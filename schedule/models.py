from django.db import models

class Place ( models.Model ):
  name = models.CharField( max_length=200 )
  seats = models.IntegerField( default=2 )

  def __unicode__ ( self ):
    return self.name

class Meeting ( models.Model ):
  end = models.DateTimeField( 'date ending', null=True, default=None )
  place = models.ForeignKey( Place )
  pub_date = models.DateTimeField( 'date published', null=True, default=None )
  start = models.DateTimeField( 'date starting', null=True, default=None )
  subject = models.CharField( max_length=200)

  def __unicode__ ( self ):
    return self.subject
