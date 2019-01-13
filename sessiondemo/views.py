from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def set_session(request):
    request.session['one'] = '1'
    request.session['two'] = '2'
    request.session['three'] = '3'
    return HttpResponse('session 存上了')


def get_session(request):
    one = request.session['one']
    two = request.session['two']
    three = request.session['three']
    print(one)
    print(two)
    print(three)
    return HttpResponse('session 取出来了')
