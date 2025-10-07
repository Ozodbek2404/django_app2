from django.shortcuts import render
from django.http import HttpResponse


def app4(request):
    return HttpResponse("SALOM app4")
