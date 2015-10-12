from events.models import Event
from events.serializers import EventSerializer
from interests.models import Interest
from interests.serializers import InterestSerializer
from custom_users.models import CustomUser
from custom_users.serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt


class EventAttending(generics.ListCreateAPIView):
    """<b>Attending Events</b>"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    allowed_methods = ['get', 'delete', 'put']

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ThemeList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response


    def get(self, request, pk=None):
        """
        Gets every Event that a given user is attending



        <b>Details</b>

        METHODS : GET



        <b>RETURNS:</b>

        - 200 OK.

        ---
        omit_parameters:
        - form
        """
        try:
            int_pk = int(pk)
            r = []
            user = CustomUser.objects.get(pk=int_pk)
            for event in self.queryset.all():
                if user in event.attending.all():
                    r += [event]
            self.queryset = r
        except:
            self.queryset = []
        return self.list(request)


    def delete(self, request, pk=None):
        """
        User is not attending an event anymore



        <b>Details</b>

        METHODS : DELETE



        <b>RETURNS:</b>

        - 200 OK.

        - 400 BAD REQUEST

        ---
        omit_parameters:
        - form
        """

        print request.META

        try:
            int_pk = int(pk)
            user = CustomUser.objects.get(pk=int_pk)
            event = Event.objects.get(pk = request.data['event_id'])
            event.attending.remove(user)
            return Response(status=status.HTTP_200_OK)
        except:
            pass
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """
        Associates a user to attend an event



        <b>Details</b>

        METHODS : PUT



        {

            "event_id": 3

        }



        <b>RETURNS:</b>

        - 200 OK.

        - 400 BAD REQUEST.

        ---
        omit_parameters:
        - form
        """

        print request.META

        try:
            int_pk = int(pk)
            user = CustomUser.objects.get(pk=int_pk)
            event = Event.objects.get(pk=request.data['event_id'])
            event.attending.add(user)
            return Response(status=status.HTTP_200_OK)
        except:
            pass
        return Response(status=status.HTTP_400_BAD_REQUEST)


class EventByHost(generics.ListCreateAPIView):
    """<b>Events by host</b>"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    allowed_methods = ['get']

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ThemeList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response


    def get(self, request, pk=None):
        """
        Gets every Event of a given host



        <b>Details</b>

        METHODS : GET



        <b>RETURNS:</b>

        - 200 OK.

        ---
        omit_parameters:
        - form
        """
        try:
            int_pk = int(pk)
            host = CustomUser.objects.get(pk=int_pk)
            self.queryset = self.queryset.filter(host=host)
        except:
            self.queryset = []
        return self.list(request)


class EventList(generics.ListCreateAPIView):
    """<b>Event List</b>"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    allowed_methods = ['get', 'post']

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ThemeList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response


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

    @csrf_exempt
    def post(self, request):
        """
        Creates an Event



        <b>Details</b>

        METHODS : POST



        {
            "title": "New Event",
            "subtitle": "Subtitle of new event",
            "description": "Description of new event",
            "interest": 2,
            "latitude": 8.99309210,
            "longitude": 9.3019203,
            "host": 3,
            "attending": 3,
            "beggining": "25062015T23:10:32",
            "end": "25062015T23:10:32",
            "cost": 4,
            "type": "PUB",
            "min_people": 2,
            "max_people": 5
        }



        <b>RETURNS:</b>

        - 200 OK.

        - 400 BAD REQUEST.

        ---
        omit_parameters:
        - form
        """

        ##### NOT WORKING STILL!!!


        if 'title' in request.data and 'subtitle' in request.data and 'description' in request\
                and 'interest' in request.data and 'latitude' in request.data and 'longitude' in request.data\
                and 'host' in request.data and 'beggining' in request.data and "type" in request.data and \
                'min_people' in request.data:

            try:

                event = Event.objects.create(title = request.data['title'],
                                     subtitle = request.data['subtitle'],
                                     description = request.data['description'],
                                     interest = request.data['interest'],
                                     #location = Geometry(request.data['longitude'], request.data['latitude']),
                                     host = request.data['host'],
                                     beggining = request.data['beggining'],
                                     type = request.data['type'],
                                     min_people = request.data['min_people'])

                if 'cost' in request.data:
                    event.cost = request.data['cost']

                if 'max_people' in request.data:
                    event.cost = request.data['max_people']

                if 'end' in request.data:
                    event.cost = request.data['end']

                return Response(status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)


class EventDetails(generics.ListCreateAPIView):
    """<b>Event Details</b>"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    allowed_methods = ['get', 'delete']

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ThemeList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response


    def get(self, request, pk=None):
        """
        Gets Event



        <b>Details</b>

        METHODS : GET



        <b>RETURNS:</b>

        - 200 OK.

        ---
        omit_parameters:
        - form
        """
        try:
            int_pk = int(pk)
            self.queryset = self.queryset.filter(pk=int_pk)
        except:
            self.queryset = []
        return self.list(request)


    def delete(self, request, pk=None):
        """
        Deletes an event



        <b>Details</b>

        METHODS : DELETE



        <b>RETURNS:</b>

        - 200 OK.

        - 400 BAD REQUEST.

        ---
        omit_parameters:
        - form
        """
        try:
            int_pk = int(pk)
            Event.objects.filter(pk = int_pk).delete()
            return Response(status=status.HTTP_200_OK)
        except:
            pass
        return Response(status=status.HTTP_400_BAD_REQUEST)


class InterestList(generics.ListCreateAPIView):
    """<b>Interest List</b>"""
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    allowed_methods = ['get', 'post']

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ThemeList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response


    def get(self, request):
        """
        Gets every Interest



        <b>Details</b>

        METHODS : GET



        <b>RETURNS:</b>

        - 200 OK.

        ---
        omit_parameters:
        - form
        """
        return self.list(request)

    @csrf_exempt
    def post(self, request):
        """
        Creates an Interest



        <b>Details</b>

        METHODS : POST



        <b>RETURNS:</b>

        - 200 OK.

        - 400 BAD REQUEST.

        ---
        omit_parameters:
        - form
        """

        if 'name' in request.data:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class InterestDetails(generics.ListCreateAPIView):
    """<b>Interest Details</b>"""
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    allowed_methods = ['get']

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ThemeList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response


    def get(self, request, pk=None):
        """
        Gets Interest for a given pk



        <b>Details</b>

        METHODS : GET



        <b>RETURNS:</b>

        - 200 OK.

        ---
        omit_parameters:
        - form
        """
        try:
            int_pk = int(pk)
            self.queryset = self.queryset.filter(pk=int_pk)
        except:
            self.queryset = []
        return self.list(request)


class InterestByUser(generics.ListCreateAPIView):
    """<b>Interests of user</b>"""
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    allowed_methods = ['get', 'delete', 'put']

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ThemeList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response


    def get(self, request, pk=None):
        """
        Gets Interest for a given user



        <b>Details</b>

        METHODS : GET



        <b>RETURNS:</b>

        - 200 OK.

        ---
        omit_parameters:
        - form
        """
        try:
            int_pk = int(pk)
            self.queryset = CustomUser.objects.get(pk = int_pk).interests.all()
        except:
            self.queryset = []
        return self.list(request)

    @csrf_exempt
    def delete(self, request, pk=None):
        """
        Deletes Interest for a given user



        <b>Details</b>

        METHODS : DELETE




        Example:

        {

        "interest_id": 2

        }




        <b>RETURNS:</b>

        - 200 OK.

        - 400 BAD REQUEST

        ---
        omit_parameters:
        - form
        """

        try:

            int_pk = int(pk)
            interest = Interest.objects.get(pk = request.data['interest_id'])
            CustomUser.objects.get(pk = int_pk).interests.remove(interest)
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    @csrf_exempt
    def put(self, request, pk=None):
        """
        Adds Interest to a given user



        <b>Details</b>

        METHODS : PUT




        Example:

        {

        "interest_id": 2

        }




        <b>RETURNS:</b>

        - 200 OK.

        - 400 BAD REQUEST

        ---
        omit_parameters:
        - form
        """

        try:

            int_pk = int(pk)
            interest = Interest.objects.get(pk = request.data['interest_id'])
            CustomUser.objects.get(pk = int_pk).interests.add(interest)
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserList(generics.ListCreateAPIView):
    """<b>User List</b>"""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    allowed_methods = ['get']

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ThemeList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response


    def get(self, request):
        """
        Gets every User



        <b>Details</b>

        METHODS : GET



        <b>RETURNS:</b>

        - 200 OK.

        ---
        omit_parameters:
        - form
        """
        return self.list(request)


class UserDetails(generics.ListCreateAPIView):
    """<b>User Details</b>"""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    allowed_methods = ['get']

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ThemeList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response


    def get(self, request, pk=None):
        """
        Gets user for a given pk



        <b>Details</b>

        METHODS : GET



        <b>RETURNS:</b>

        - 200 OK.

        ---
        omit_parameters:
        - form
        """
        try:
            int_pk = int(pk)
            self.queryset = self.queryset.filter(pk=int_pk)
        except:
            self.queryset = []
        return self.list(request)


class UserHost(generics.ListCreateAPIView):
    """<b>User that hosts given event</b>"""
    queryset = Event.objects.all()
    serializer_class = CustomUserSerializer
    allowed_methods = ['get']

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ThemeList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response


    def get(self, request, pk=None):
        """
        Gets user that hosts given event



        <b>Details</b>

        METHODS : GET



        <b>RETURNS:</b>

        - 200 OK.

        ---
        omit_parameters:
        - form
        """
        try:
            int_pk = int(pk)
            self.queryset = [self.queryset.get(pk=int_pk).host]

        except:
            self.queryset = []
        return self.list(request)


class UserAttending(generics.ListCreateAPIView):
    """<b>User that attends given event</b>"""
    queryset = Event.objects.all()
    serializer_class = CustomUserSerializer
    allowed_methods = ['get']

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ThemeList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response


    def get(self, request, pk=None):
        """
        Gets users that attend given event



        <b>Details</b>

        METHODS : GET



        <b>RETURNS:</b>

        - 200 OK.

        ---
        omit_parameters:
        - form
        """
        try:
            int_pk = int(pk)
            self.queryset = self.queryset.get(pk=int_pk).attending.all()
        except:
            self.queryset = []
        return self.list(request)