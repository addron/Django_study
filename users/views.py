from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
# from django.core.urlresolvers import reverse

# Create your views here.
# 必须传request

def index(request):
    return HttpResponse("index is show!")


def say(request):
    # 类似flask中url_for
    url = reverse("usernamespace:username")
    print(url)
    # redirect(url)
    return HttpResponse("index is show say !")

def sayhello(request):
    url = reverse("usernamespace:username")
    print(url)
    return redirect(url)
