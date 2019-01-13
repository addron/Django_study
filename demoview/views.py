from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.

def mydeacorator(func):
    def wrapper(request, *args, **kwargs):
        print("我是1号装饰器")
        print(request.path)
        return func(request, *args, **kwargs)

    return wrapper


def mydeacorator2(func):
    def wrapper(request, *args, **kwargs):
        print("我是2号装饰器")
        print(request.path)
        return func(request, *args, **kwargs)

    return wrapper


# 扩展类
class Baseview(object):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        view = mydeacorator(view)
        return view


class Base2view(object):

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        view = mydeacorator2(view)
        return view


class Demoview(Baseview, Base2view, View):

    def get(self, request):
        print('get进来了')
        return HttpResponse('GET 好了')

    def post(self, request):
        print('post进来了')
        return HttpResponse('POST 好了')
