from django.conf.urls import url

from demoview import views

urlpatterns = [
    url(r'^demoview/$', views.Demoview.as_view())
    # url(r'^get_cook/$', views.get_cook)
    # url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather),
    # url(r'^params/', views.params),
    # url(r'^index/$', views.index)
]
