#coding=utf-8

import string


import bottle
from weibo import APIClient
from bottle import jinja2_view as view
from bottle import request,response,urllib,Response

from oauth_parameter import oauth_para

import json

global sendAddr


def GetWeiboAccessToken():
  beaker_session = request.environ['beaker.session']
  return beaker_session['cookies_access']
  
  
def GetWeiboExpires():
  beaker_session = request.environ['beaker.session']
  return beaker_session['cookies_expires']
  
  
class WeiboApiHandler(object):
  def __init__(self):
    self.__weibo_access_token = GetWeiboAccessToken()
    self.__weibo_expires = GetWeiboExpires()
    
   #for search_position varibal
    self.__search_position_address = ""
    
  @classmethod
  def login_to_weibo(cls):
    client = APIClient(app_key=oauth_para['weibo']['appid'], app_secret=oauth_para['weibo']['secret'], redirect_uri=oauth_para['weibo']['redirect_url'])
    url = client.get_authorize_url()
    bottle.redirect(url)
    

  @classmethod
  @view('static/template/homepage.html')
  def weibo(cls):
    code = bottle.request.GET.get('code')
    client = APIClient(app_key=oauth_para['weibo']['appid'], app_secret=oauth_para['weibo']['secret'], redirect_uri=oauth_para['weibo']['redirect_url'])
    r = client.request_access_token(code)
  
    weibo_access_token = r.access_token
    weibo_expires_in = r.expires_in
    client.set_access_token(weibo_access_token, weibo_expires_in)
    
    ruid = client.get.account__get_uid()
    userinfo = client.get.users__show( access_token =weibo_access_token, uid = ruid.uid )
    

    beaker_session = request.environ['beaker.session']
    beaker_session['cookies_access'] = weibo_access_token
    beaker_session['cookies_expires'] = weibo_expires_in
    beaker_session['username'] = userinfo.screen_name
    beaker_session.save()
    
    return { 'username': userinfo.screen_name }
    
  def weibo_place_nearby_photos( self ):
    client = APIClient(app_key=oauth_para['weibo']['appid'], app_secret=oauth_para['weibo']['secret'], redirect_uri=oauth_para['weibo']['redirect_url'])
    client.set_access_token( self.__weibo_access_token, self.__weibo_expires )    
    ruid = client.get.account__get_uid()  
    userinfo = client.get.users__show( access_token =self.__weibo_access_token, uid = ruid.uid )
    
    place_user = client.get.place__user_timeline( access_token =self.__weibo_access_token, uid = ruid.uid )  
    
    lat1 = place_user.statuses[0].geo.coordinates[0]
    long1 = place_user.statuses[0].geo.coordinates[1]
           
    place_photos = client.get.place__nearby__photos( access_token =self.__weibo_access_token, lat = lat1, long = long1, range = 500, count = 50 )
    
    #return {'data':place_photos.statuses, 'username':place_user.screen_name} 
    
    if 'statuses' in place_photos:
      data = json.dumps( place_photos.statuses)
      return {'data': place_photos.statuses, 'username':userinfo.screen_name} 
    else:
      return {'error_info': 'input_error', 'username':userinfo.screen_name}
    
  def weibo_position_search( self ):
    
    sendAddr = request.params.get('address')
    
    
    
    return {'address':str(sendAddr) }
    
  def weibo_position_search_data(self):
    client = APIClient(app_key=oauth_para['weibo']['appid'], app_secret=oauth_para['weibo']['secret'], redirect_uri=oauth_para['weibo']['redirect_url'])
    client.set_access_token( self.__weibo_access_token, self.__weibo_expires )    
    ruid = client.get.account__get_uid()
    address = request.params.get('address')
    #return address
    
    position = client.get.location__geo__address_to_geo( address = address )
    
    ruid = client.get.account__get_uid()
    userinfo = client.get.users__show( access_token =self.__weibo_access_token, uid = ruid.uid )
   
    lats = str(position.geos[0]['latitude'])
    lngs = str(position.geos[0]['longitude'])
    
    lat = string.atof( lats )
    lng = string.atof( lngs )
    
    place_photos = client.get.place__nearby__photos( access_token =self.__weibo_access_token, lat = lat, long = lng, range = 500, count = 50 )
   
    
    if 'statuses' in place_photos:
      data = json.dumps( place_photos.statuses)
      return {'data': data, 'username':userinfo.screen_name} 
    else:
      return {'error_info': 'input_error', 'username':userinfo.screen_name}
      
      
  def weibo_user_show( self ):
    client = APIClient(app_key=oauth_para['weibo']['appid'], app_secret=oauth_para['weibo']['secret'], redirect_uri=oauth_para['weibo']['redirect_url'])
    client.set_access_token( self.__weibo_access_token, self.__weibo_expires )    
    ruid = client.get.account__get_uid()
    address = request.params.get('address')
    
    userinfo = client.get.users__show( access_token =self.__weibo_access_token, uid = ruid.uid )
    
    user_timeline = client.get.statuses__user_timeline( uid=ruid.uid, count = 20 )
    
    
    if 'statuses' in user_timeline:
      return {'data': user_timeline.statuses, 'username':userinfo.screen_name} 
    else:
      return {'error_info': 'input_error', 'username':userinfo.screen_name}
      
  @classmethod    
  def weibo_homepage( cls ):
    beaker_session = request.environ['beaker.session']
    
    if 'username' in beaker_session:
      return { 'username' : beaker_session['username'] }
    else:
      return {}
    
    
session_opts = {
  'session.type': 'cookie',
  'session.expires': 300,
  'session.validate_key': '1234',
}


    
    