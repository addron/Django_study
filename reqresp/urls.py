from django.conf.urls import url

from reqresp import views

urlpatterns = [
    url(r'^index/$', views.index),
    # url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather),
    url(r'^params/', views.params),
    # url(r'^index/$', views.index)
]
