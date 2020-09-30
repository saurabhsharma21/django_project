from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#view function 
def home(request):
    return HttpResponse("This is a home Page")
    #return response --> HTML contect, redirect, 404, doc/image
    #contains a response for a request
def about(request):
    return HttpResponse("This is about page")

def contact(request):
    return HttpResponse("Contact us")