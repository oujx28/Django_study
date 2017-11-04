# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    #return HttpResponse(u"Wellcom to study django")
    return render(request, 'index.html')

def home(request):
    string = u'测试中。。。。'
    TutorialList = ["HTML", 'CSS', 'JQuery', 'Python', 'Django']
    info_dict = {'site':u'study school', 'content': u'IT BOOK'}
    List = map(str, range(100))
    return render(request, 'home.html', {'string': string, 'TutorialList': TutorialList,
                                         'info_dict': info_dict, 'List': List})

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )

