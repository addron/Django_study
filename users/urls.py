from django.conf.urls import url

from users import views

urlpatterns = [
    # 每个路由信息都需要使用url函数来构造
    # url(路径, 视图)
    url(r'^index/$', views.index),
    url(r'^say/$', views.say, name="username"),
    url(r'^sayhello/$', views.sayhello)
]
