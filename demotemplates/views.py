from django import template
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader

def index(request):
    # return HttpResponse("demotemplates index is show!")
    return redirect('/index.html')

# def show(request):
#
#     template=loader.get_template('index.html')
#
#     context={'city': 'BJ'}
#
#     return HttpResponse(template.render(context))

def show(request):
    context = {
        'city': '北京',
        'adict': {
            'name': '西游记',
            'author': '吴承恩'
        },
        'alist': [1, 2, 3, 4, 5]
    }
    return render(request,'index.html',context=context)
