from django.core import paginator
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from fairy.models import *
from sims.models import *


def page1(request):
    return render(request, 'page1.html', locals())


def page2(request):
    return render(request, 'page2.html', locals())


def page3(request):
    return render(request, 'page3.html', locals())


def page4(request):
    return render(request, 'page4.html', locals())


def page5(request):
    return render(request, 'page5.html', locals())


def page6(request):
    return render(request, 'page6.html', locals())


def redirect_home(request):
    return redirect(reverse('Home'))


def page7(request, pagenum =1):
    title = "日志"
    menu_list = []
    pages = Page.objects.all()
    return render(request, 'page7.html', locals())


def page8(request):
    return render(request, 'page8.html', locals())


def page9(request):
    return render(request, 'page9.html', locals())

