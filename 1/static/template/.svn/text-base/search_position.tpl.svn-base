
{% extends "static/template/layout.html" %}

{% block content %}

    <script type="text/javascript" src="static/js/search_position.js"></script>

    {% if error_info == 'input_error' %}
          <div class="span4">
          </div>
          <div class="span4">
            <a href="/">请重新输入</a>
          </div>
          <div class="span4">
          </div>
    {% else %}
       
  	  <div class="row-fluid">
                <div class="span1">
                </div>
  	  	<div class="span3">
                  <div id="container1"  >
                  </div>
  	  	</div>
                
  	  	<div class="span7">
                
                  <div id="map"></div>
                  
                    <script id="info" type="text/x-jquery-tmpl">
                      
                      <div >
                      <a href="http://weibo.com/u/${user.id}">
                      <img src=${original_pic} class="img-rounded"/>
                      </a>
                      </div>
                    </script>
                  
                  
                  
                  <script type="text/javascript">
                  
                  
                    
                    fetch = function() {
                          xhr = null;
                          var i = 0;
                      var bdata = ({{data}});
                          
                          var tst = bdata
                          var lat1 = 0
                          var lng1 = 0
                          
                          for (var i = 0; i < tst.length; i++ )
                          {
                            if ( tst[i].geo != null )
                            {
                              if ( tst[i].geo.hasOwnProperty('coordinates') )
                              {
                                lat1 = tst[i].geo.coordinates[0];
                                lng1 = tst[i].geo.coordinates[1];
                                break;
                              }
                            }
                          }
                          
                          
                          map = new GMaps({
                          div: '#map',
                          lat: lat1,
                          lng: lng1,
                          height: '675px'
                          
                          });
                          
                          
      
                         for ( var i = 0; i < tst.length; i++ )
                         {
                           if ( tst[i].geo != null && tst[i].geo.hasOwnProperty('coordinates') )
                           {
                             lat1 = tst[i].geo.coordinates[0];
                             lng1 = tst[i].geo.coordinates[1];
                             var img_url = tst[i].original_pic;
                             var text = tst[i].text;
                             
                             map.addMarker(
                             {
                               lat: lat1,
                               lng: lng1,
                               title: 'Marker with InfoWindow',
                               infoWindow: {
                                 content: '<div><p>'+text+'</p>'+'</br><img id='+'"'+'infow' +'"'+' src='+img_url+'></div>'
                               }
                             }
                             );
                             
                             
                             
             
                           }
                           
                           
                         }
    
                         $("#info").tmpl(tst).appendTo("#container1");
                      
                    
                    
                    };
                    fetch();
                    
                    
                  </script>
                
                  
                
  	  	</div>
              <div class="span1"></div>
  	  </div>
    {% endif %}
 
    {% endblock %}





