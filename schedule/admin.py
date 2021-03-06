from django.contrib import admin
from schedule.models import Place, Meeting

class PlaceAdmin ( admin.ModelAdmin ):
  fields = ['name', 'seats']

class MeetingAdmin ( admin.ModelAdmin ):
  fields = ['subject', 'place', 'pub_date', 'start', 'end', 'created_by']

admin.site.register( Place, PlaceAdmin )
admin.site.register( Meeting, MeetingAdmin )
