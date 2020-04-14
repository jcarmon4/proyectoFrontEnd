from django.shortcuts import render, HttpResponse
import requests

# Create your views here.
def home(request):
    return render(request, "measure/home.html")

def measure(request):
    return render(request, "measure/measure.html")
