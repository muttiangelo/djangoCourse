from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("sofia linda")

def indexOne(request):
    return HttpResponse("Calculo A")
