from django.conf.urls import url

from sessiondemo import views

urlpatterns = [
    url(r'^set_session/$', views.set_session),
    url(r'^get_session/$', views.get_session)
    # url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather),
    # url(r'^params/', views.params),
    # url(r'^index/$', views.index)
]
