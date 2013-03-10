#!/usr/bin/python
#-*- coding:utf8 -*-

import sae
from bottle import Bottle,debug,request
from bottle import jinja2_view as view

from beaker.middleware import SessionMiddleware
from weibo_controller import WeiboApiHandler, session_opts
from instagram_controller import Instagram



debug(True)
app = Bottle()

@app.route('/') 
@view('static/template/homepage.html')
def main_page_show():
  return WeiboApiHandler.weibo_homepage()
  
@app.route('/login_to_weibo')
def login_to_weibo_view():
  return WeiboApiHandler.login_to_weibo()
  
@app.route('/logout')
@view('static/template/homepage.html')
def logout():
  return {}
  
@app.route('/index')
@app.route('/weibo')
def weibo_view():
  return WeiboApiHandler.weibo()

@app.route('/weibo_poi_get')
@view('static/template/place_photos.tpl')
def weibo_location_pois_search_by_location_view():
  weiboApi = WeiboApiHandler()
  return weiboApi.weibo_place_nearby_photos()
  
@app.route('/weibo_poi_data')
def weibo_place_photos():
  weiboApi = WeiboApiHandler()
  return weiboApi.weibo_place_nearby_photos()
  
@app.route('/weibo_position_search')
#@view('static/template/search_position.tpl')
def weibo_position_search():
  weiboApi = WeiboApiHandler()
  return weiboApi.weibo_position_search()

@app.route('/weibo_position_search_data')
@view('static/template/search_position.tpl')
def weibo_position_search():
  weiboApi = WeiboApiHandler()
  return weiboApi.weibo_position_search_data() 
  
@app.route('/weibo_user_show')
#@view('static/template/json_data_show.html')
@view('static/template/user_weibo_show.html')
def weibo_user_show():
  weiboApi = WeiboApiHandler()
  return weiboApi.weibo_user_show()

@app.route('/login_to_instagram')
def login_to_instagram():
  return Instagram.login_to_instagram()
  
@app.route('/instagram')
@view('static/template/instagram_show.html')
def instagram_show():
  return Instagram.get_user()
  
  
@app.route('/error_info')
@view('static/template/error_info.html')
def show_error_info():
  return {}
  
app = SessionMiddleware( app, session_opts )
#application = sae.create_wsgi_app(app)