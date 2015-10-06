from django.conf.urls import include, url
from api import views

urlpatterns = [
    #url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^event/$', views.EventList.as_view()),
    url(r'^event/(?P<pk>[0-9]+)/$', views.EventDetails.as_view()),
    url(r'^event/host/(?P<pk>[0-9]+)/$', views.EventByHost.as_view()),
    url(r'^event/attending/(?P<pk>[0-9]+)/$', views.EventAttending.as_view()),
    url(r'^interest/$', views.InterestList.as_view()),
    url(r'^interest/(?P<pk>[0-9]+)/$', views.InterestDetails.as_view()),
    url(r'^interest/user/(?P<pk>[0-9]+)/$', views.InterestByUser.as_view()),
    url(r'^user/$', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetails.as_view()),
    url(r'^user/host/event/(?P<pk>[0-9]+)/$', views.UserHost.as_view()),
    url(r'^user/attending/event/(?P<pk>[0-9]+)/$', views.UserAttending.as_view()),
]