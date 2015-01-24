from django.conf.urls import patterns, url
from schedule import views

urlpatterns = patterns( '',
  url( r'^rooms/$', views.rooms, name='rooms' ),
  url( r'^room/(?P<room_id>\d+)/check/$', views.roomCheck, name='room_check' ),
  url( r'^room/(?P<room_id>\d+)/book/$', views.roomBook, name='room_book' ),
  url( r'^room/(?P<room_id>\d+)/$', views.room, name='room' )
)
