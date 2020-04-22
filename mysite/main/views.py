from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Tutorial

# Create your views here.
def homepage(request):
    return render(request = request,
    			  template_name = "main/home.html",
    			  context = {"tutorials": Tutorial.objects.all})