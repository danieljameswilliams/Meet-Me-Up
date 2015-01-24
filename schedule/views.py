from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from schedule.models import Place, Meeting
from datetime import datetime

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
    subject = request.POST['subject']

    # Check if it is really free again, and not just skipped checking.
    conflicts = roomCheck( request, room_id, True )
    if not conflicts == 0:
      return

    meeting = Meeting(
      created_by = User.objects.get( id = request.user.id ),
      end = end_date,
      place = Place.objects.get( id = room_id ),
      pub_date = datetime.now(),
      start = start_date,
      subject = subject
    )
    meeting.save( force_insert = True )

    template = loader.get_template( 'schedule/room_book.html' )
    context = RequestContext( request )

    return HttpResponse( template.render( context ) )
  else:
    return HttpResponseRedirect('/')

'''
  In this function, we only show the template
  containing a login form, to submit to /login/auth/
'''
def login ( request ):
  template = loader.get_template( 'schedule/login.html' )
  context = RequestContext( request )
  return HttpResponse( template.render( context ) )

def create ( request ):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']

    user = User.objects.create_user( username, email, password )
    user.first_name = first_name
    user.email = email
    user.last_name = last_name
    user.save()

    return HttpResponseRedirect( '/' )
