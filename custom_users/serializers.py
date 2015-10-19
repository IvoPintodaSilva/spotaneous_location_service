from rest_framework import serializers
from custom_users.models import CustomUser
from interests.serializers import InterestSerializer
import geojson

class CustomUserSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField('get_geojson')
    interests = InterestSerializer(many=True)

    class Meta:
        model = CustomUser

    def get_geojson(self, obj):
        if not obj or not obj.location:
            return None
        return geojson.Point((obj.location.x, obj.location.y))