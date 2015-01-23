from django.conf.urls import patterns, url
from schedule import views

urlpatterns = patterns( '',
  url( r'^$', views.rooms, name='rooms' ),
  url( r'^room/(?P<room_id>\d+)/$', views.room, name='room' )
)
