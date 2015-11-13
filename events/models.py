from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from interests.models import Interest
from custom_users.models import CustomUser


TYPE = (
    ('PRIV', 'Private'),
    ('PUB', 'Public'),
)

class Event(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=250)
    interest = models.ForeignKey(Interest)
    location = models.PointField(blank=True, null=True)
    host = models.ForeignKey(CustomUser, related_name='event_host')
    attending = models.ManyToManyField(CustomUser, blank= True, related_name='event_attending')
    beginning = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=10, choices=TYPE)
    min_people = models.IntegerField()
    max_people = models.IntegerField(blank=True, null=True)
    objects = models.GeoManager()


    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")

    def __unicode__(self):
        return self.title