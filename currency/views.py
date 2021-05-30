from django.shortcuts import render
from django.http import HttpResponse


def generate_password(request):
    return HttpResponse('Hello World!')
