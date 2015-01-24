from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext, loader

from schedule.models import Place, Meeting

@csrf_exempt
def rooms ( request ):
  input_seats = 0

  if request.GET.has_key('seats'):
    input_seats = request.GET['seats']
    places = Place.objects.filter( seats__gte = input_seats)
  else:
    places = Place.objects.all()

  template = loader.get_template( 'schedule/rooms.html' )
  context = RequestContext( request, {
    'places': places,
    'seats': input_seats
  })

  return HttpResponse( template.render( context ) )

def room ( request, room_id ):
  meetings = Meeting.objects.filter( place = room_id )

  template = loader.get_template( 'schedule/room.html' )
  context = RequestContext( request, {
    'meetings': meetings,
    'room': room_id
  })

  return HttpResponse( template.render( context ) )

def roomCheck ( request, room_id, is_local=None ):
  if request.method == 'POST':
    start_date = request.POST['start_date']
    end_date = request.POST['end_date']

    meetings = Meeting.objects.filter( place = room_id, start__lt = end_date, end__gt = start_date )

    template = loader.get_template( 'schedule/room_check.html' )
    context = RequestContext( request, {
      'meetings': meetings,
      'room': room_id,
      'start_date': start_date,
      'end_date': end_date
    })

    if is_local:
      return meetings.count()
    else:
      return HttpResponse( template.render( context ) )
  else:
    return HttpResponseRedirect('/')

def roomBook ( request, room_id ):
  if request.method == 'POST':
    start_date = request.POST['start_date']
    end_date = request.POST['end_date']

    # Check if it is really free again, and not just skipped checking.
    conflicts = roomCheck( request, room_id, True )
    if not conflicts == 0:
      return

    # TODO: Add the meeting to DB

    template = loader.get_template( 'schedule/room_book.html' )
    context = RequestContext( request )

    return HttpResponse( template.render( context ) )
  else:
    return HttpResponseRedirect('/')
