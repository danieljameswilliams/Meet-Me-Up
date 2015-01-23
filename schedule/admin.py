from django.contrib import admin
from schedule.models import Place, Meeting

class PlaceAdmin ( admin.ModelAdmin ):
  fields = ['name']

class MeetingAdmin ( admin.ModelAdmin ):
  fields = ['subject', 'place', 'pub_date']

admin.site.register( Place, PlaceAdmin )
admin.site.register( Meeting, MeetingAdmin )
