from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.template import loader


def set_cook(request):
    response = HttpResponse()
    response.set_cookie('itcast01', 'python')
    response.set_cookie('itcast02', 'java')
    print('存好了')
    return response

def get_cook(request):

    cook = request.COOKIES.get('itcast01')
    print(cook)

    return HttpResponse('getcook is show!')


