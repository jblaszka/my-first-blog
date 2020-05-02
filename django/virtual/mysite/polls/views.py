from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Justyna to Dawid, czy Dawid to Justyna?")