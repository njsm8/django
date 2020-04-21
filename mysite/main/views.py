from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("pythonprogramming.net homepage! Wow so #amaze.")