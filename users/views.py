from django.shortcuts import render

# Create your views here.



from django.http import HttpResponse


def index(request):
    return HttpResponse("Hname prizma address ktm")


def today(request):
    return HttpResponse("today is 2080/10/24 ,abd its wednesday")