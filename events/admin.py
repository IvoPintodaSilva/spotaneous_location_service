from django.contrib.gis import admin
from events.models import Event

class EventAdmin(admin.OSMGeoAdmin):
    model = Event
    filter_horizontal = ('attending',)

admin.site.register(Event, EventAdmin)