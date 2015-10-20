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
from django.contrib.gis.geos import GEOSGeometry
import json
import dateutil.parser


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
            "beggining": "2008-04-10 11:47:58",
            "end": "'2008-04-10 11:47:58'",
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

        if 'title' in request.data and 'subtitle' in request.data and 'description' in request.data\
                and 'interest' in request.data and 'latitude' in request.data and 'longitude' in request.data\
                and 'host' in request.data and 'beginning' in request.data and "type" in request.data and \
                'min_people' in request.data:



            try:

                event = Event.objects.create(title = request.data['title'],
                                             subtitle = request.data['subtitle'],
                                             description = request.data['description'],
                                             interest = Interest.objects.get(pk=int(request.data['interest'])),
                                             location = GEOSGeometry('POINT(' + str(request.data['longitude']) + ' ' +
                                                                     str(request.data['longitude']) + ')'),
                                             host = CustomUser.objects.get(pk=int(request.data['host'])),
                                             beginning = dateutil.parser.parse(request.data['beginning']),
                                             type = request.data['type'],
                                             min_people = request.data['min_people'])

                if 'cost' in request.data:
                    event.cost = request.data['cost']

                if 'max_people' in request.data:
                    event.max_people = request.data['max_people']

                if 'end' in request.data:
                    event.end = dateutil.parser.parse(request.data['end'])

                event.save()


                return Response(status=status.HTTP_200_OK, data=event.pk)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)


class EventDetails(generics.ListCreateAPIView):
    """<b>Event Details</b>"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    allowed_methods = ['get', 'delete', 'put']

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


    def put(self, request, pk=None):
        """
        Edits an event



        <b>Details</b>

        METHODS : PUT



        <b>RETURNS:</b>

        - 200 OK.

        - 400 BAD REQUEST.

        ---
        omit_parameters:
        - form
        """

        try:
            int_pk = int(pk)
            event = Event.objects.get(pk = int_pk)

            if 'title' in request.data:
                event.title = request.data['title']

            if 'subtitle' in request.data:
                event.subtitle = request.data['subtitle']

            if 'description' in request.data:
                event.description = request.data['description']

            if 'interest' in request.data:
                event.interest = request.data['interest']

            #if 'latitude' in request.data and 'longitude' in request.data:
            #    location = ...

            #if 'beggining' in request.data:
            #    event.beggining = ...

            if "type" in request.data:
                event.type = request.data['type']

            if 'min_people' in request.data:
                event.min_people = request.data['min_people']

            if 'max_people' in request.data:
                event.max_people = request.data['max_people']

            event.save()

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
    allowed_methods = ['get', 'post']

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ThemeList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response

    @csrf_exempt
    def post(self, request):
        """
        Creates a User



        <b>Details</b>

        METHODS : POST


        {

        "id": 20,

        "latitude": 8,

        "longitude":9,

        "interests":["swag", "football", "fashion"]

        }


        <b>RETURNS:</b>

        - 200 OK.

        - 400 BAD REQUEST.

        ---
        omit_parameters:
        - form
        """


        if 'id' in request.data:
            try:
                # user already exists
                CustomUser.objects.get(pk=request.data['id'])
                return Response(status=status.HTTP_400_BAD_REQUEST)
            except:
                # user doesnt exist
                user = CustomUser.objects.create(id=request.data['id'])
                # check for interests
                if 'latitude' in request.data and 'longitude' in request.data:
                    user.location = GEOSGeometry('POINT(' + str(request.data['longitude']) + ' ' +
                                                 str(request.data['longitude']) + ')')
                    user.save()
                if 'interests' in request.data:
                    for interest in request.data['interests']:
                        try:
                            i = Interest.objects.get(name__iexact=interest)
                            user.interests.add(i)
                            user.save()
                        except:
                            i = Interest.objects.create(name=interest)
                            i.save()
                            user.interests.add(i)
                            user.save()
                    return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)



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
    allowed_methods = ['get', 'put']

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

    def put(self, request, pk=None):
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
            user = self.queryset.get(pk=int_pk)
            if 'latitude' in request.data and 'longitude' in request.data:
                    user.location = GEOSGeometry('POINT(' + str(request.data['longitude']) + ' ' +
                                                 str(request.data['longitude']) + ')')
                    user.save()
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


class UserDistance(generics.ListCreateAPIView):
    """<b>User List by distance</b>"""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    allowed_methods = ['get']

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ThemeList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response





    def get(self, request):
        """
        Gets Users for interest ordered by distance



        <b>Details</b>

        METHODS : GET


        {

        "latitude": 8.23942349,

        "longitude": 9.1238971

        }



        <b>RETURNS:</b>

        - 200 OK.

        longitude -- Longitude of point to search from
        latitude -- Latitude of point to search from
        interest -- Interest of event
        ---
        omit_parameters:
        - form
        """

        if 'longitude' in self.request.GET.keys() and 'latitude' in self.request.GET.keys():
            point = GEOSGeometry('POINT(' + str(request.GET['longitude']) + ' ' +
                                                 str(request.GET['latitude']) + ')')

            self.queryset = CustomUser.objects.distance(point).order_by('distance')

        if 'interest' in self.request.GET.keys():
            try:
                users = self.queryset
                resp = []
                for user in users:
                    interests = user.interests
                    if interests and Interest.objects.get(name__iexact=request.GET['interest']) in user.interests.all():
                        resp += [user]
                self.queryset = resp
            except:
                self.queryset = []

        return self.list(request)
