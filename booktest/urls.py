from django.conf.urls import url

from booktest import views

urlpatterns = [
    url(r'^books/$', views.BookListView.as_view()),
    url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view())
    # url(r'^get_cook/$', views.get_cook)
    # url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather),
    # url(r'^params/', views.params),
    # url(r'^index/$', views.index)
]