from django.conf.urls import patterns, url
from schedule import views

urlpatterns = patterns( '',
  url( r'^rooms/$', views.rooms, name='rooms' ),

  url( r'^room/(?P<room_id>\d+)/check/$', views.roomCheck, name='room_check' ),
  url( r'^room/(?P<room_id>\d+)/book/$', views.roomBook, name='room_book' ),
  url( r'^room/(?P<room_id>\d+)/$', views.room, name='room' ),

  url( r'^login/auth/$', 'django.contrib.auth.views.login' ),
  url( r'^login/create/$', views.create, name='create' ),
  url( r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'} ),
  url( r'^$', views.login, name='login' )
)
