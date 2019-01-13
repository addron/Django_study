from django.conf.urls import url

from cook import views

urlpatterns = [
    url(r'^set_cook/$', views.set_cook),
    url(r'^get_cook/$', views.get_cook)
    # url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather),
    # url(r'^params/', views.params),
    # url(r'^index/$', views.index)
]