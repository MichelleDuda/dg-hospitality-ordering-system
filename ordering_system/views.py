from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def ordering(request):
    return HttpResponse("Hello, Let's Order!")

