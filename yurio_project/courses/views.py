from django.shortcuts import render
from django.http import HttpResponse


def test(request):
    return HttpResponse('Courses test view 2.0')
