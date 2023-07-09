from django.shortcuts import render
from .models import Person
# from django.http import HttpResponse
# Create your views here.
def matricula(response):
    
    return render(response, "index.html", {"personas": Person.objects.all()})