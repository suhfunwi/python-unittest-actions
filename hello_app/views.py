from django.shortcuts import render, HttpResponse
from .math import addition


def hello(request):
    return HttpResponse('Hello everyone!')


def two_plus_two(request):
    total = addition(2, 2)
    return HttpResponse(f'Two plus two is {total}')
