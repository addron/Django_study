from django.conf.urls import url

from demotemplates import views

urlpatterns = [
    url(r'^index/$', views.index),
    # url(r'^show/$', views.show),
    url(r'^show/$', views.show)
    # url(r'^demotemplates/$', views.index1)
]
