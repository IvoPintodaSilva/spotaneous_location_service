from django.shortcuts import render
from events.models import Event
from events.serializers import EventSerializer

from rest_framework.response import Response
from rest_framework import status
import math
from rest_framework import generics


"""  Theme's REST methods  """
class EventList(generics.ListCreateAPIView):
    """<b>Event List</b>"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    allowed_methods = ['get']

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ThemeList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response

    def list(self, request):
        #queryset = self.filter_queryset(self.get_queryset())
        #page = self.paginate_queryset(queryset)
        #if page is not None:
        #    serializer = self.get_serializer(page, many=True)
        #    return self.get_paginated_response(serializer.data)
        #serializer = self.get_serializer(queryset, many=True)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def get(self, request):
        """
        Gets every Event



        <b>Details</b>

        METHODS : GET



        <b>RETURNS:</b>

        - 200 OK.

        ---
        omit_parameters:
        - form
        """
        return self.list(request)
