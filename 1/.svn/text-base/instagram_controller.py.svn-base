
import urllib2
import bottle
import json


from oauth_parameter import oauth_para

def GetInstagramAccessToken():
  beaker_session = request.environ['beaker.session']
  return beaker_session['cookies_access']
  
  
def GetWeiboExpires():
  beaker_session = request.environ['beaker.session']
  return beaker_session['cookies_expires']


class Instagram( object ):
  def __init__(self):
    self.__instagram_access_token = GetWeiboAccessToken()
    self.__instagram_expires = GetWeiboExpires()  
  
  

  @classmethod
  def login_to_instagram(cls):
    instagram_url = 'https://instagram.com/oauth/authorize/?'
    instagram_url += 'client_id=' + oauth_para['instagram']['appid']
    instagram_url += '&redirect_uri=' + oauth_para['instagram']['redirect_url']
    instagram_url += '&response_type=token'
    bottle.redirect(instagram_url)
    #return instagram_url
    
  
  @classmethod
  def get_user(cls):
    #access_token = bottle.request.params.get('access_token')
    url = 'https://api.instagram.com/v1/media/popular?' + 'client_id=' + oauth_para['instagram']['appid']
    original_array = urllib2.urlopen(url)
    
    
    for char_array in original_array:
      str_json = "".join(char_array)
      str_json = json.loads(str_json)
      
    
      
    
    return {'str_json':str_json['data'][0]['comments']['data']}
    
    