import json

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    """

    :param request:  必填项 实质是HttpRequest
    :return:  必须返回HttpResponse
    """
    return HttpResponse("reqresp index is show!")


# /reqresp/weather/beijng/2018  位置参数，一一对应
# /reqresp/weather/(?<city>[a-z]+)/(?<year>\d{4}/$)   无需对应
def weather(request, city, year):
    print('city=%s' % city)
    print('year=%s' % year)
    return HttpResponse("reqresp weather is show!")


# QueryDict
def params(request):
    # 'GET' 发过来的
    # QueryDict = request.GET
    # a = QueryDict.get('a') # 1 abc
    # b = QueryDict.get('b') # 2
    # alist = QueryDict.getlist('a')
    #
    # print(a)
    # print(b)
    # print(alist)

    # 表单数据 formdata
    # a = request.POST.get('a')
    # b = request.POST.get('b')
    # alist = request.POST.getlist('a')
    #
    # print(a)
    # print(b)
    # print(alist)

    # 非表单数据  python3.5以上可以接收bytes，str,以下及3.5需要转换
    # data_bytes = request.body
    # data_str = data_bytes.decode()
    #
    # dict = json.loads(data_str)  # 转为字典
    #
    # print(dict.get('a'))
    # print(dict.get('b'))

    # 请求头 META
    # length = request.META['CONTENT_LENGTH']
    # print(length)

    # 其他种类
    print(request.method)
    print(request.user)  # AnonymousUser  匿名用户
    print(request.path)  # / reqresp / params /

    return HttpResponse("reqresp params is show!")
