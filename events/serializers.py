from rest_framework import serializers
from events.models import Event
from custom_users.serializers import CustomUserSerializer
from interests.serializers import InterestSerializer
import geojson

class EventSerializer(serializers.ModelSerializer):
    host = CustomUserSerializer()
    attending = CustomUserSerializer(many=True)
    interest = InterestSerializer()
    location = serializers.SerializerMethodField('get_geojson')

    class Meta:
        model = Event

    def get_geojson(self, obj):
        if not obj or not obj.location:
            return None
        return geojson.Point((obj.location.x, obj.location.y))