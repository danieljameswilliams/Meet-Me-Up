from django.http import HttpResponse
from django.template import RequestContext, loader

from schedule.models import Place, Meeting

def rooms ( request ):
  places = Place.objects.all()
  output = ""

  template = loader.get_template( 'schedule/rooms.html' )
  context = RequestContext( request, {
    'places': places,
  })

  return HttpResponse( template.render( context ) )

def room ( request, room_id ):
  meetings = Meeting.objects.filter( place = room_id )
  output = ""

  template = loader.get_template( 'schedule/room.html' )
  context = RequestContext( request, {
    'meetings': meetings,
  })

  return HttpResponse( template.render( context ) )
