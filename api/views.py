from events.models import Event
from events.serializers import EventSerializer
from interests.models import Interest
from interests.serializers import InterestSerializer
from custom_users.models import CustomUser
from custom_users.serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


class EventAttending(generics.ListCreateAPIView):
    """<b>Attending Events</b>"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    allowed_methods = ['get']

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
    allowed_methods = ['get']

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


class EventDetails(generics.ListCreateAPIView):
    """<b>Event Details</b>"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    allowed_methods = ['get']

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ThemeList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response


    def get(self, request, pk=None):
        """
        Gets Event for a given pk



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


class InterestList(generics.ListCreateAPIView):
    """<b>Interest List</b>"""
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    allowed_methods = ['get']

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
    allowed_methods = ['get']

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