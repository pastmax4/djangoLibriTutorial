from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#11Mag2019
def home_view(request,*args, **kargs):
    #print('una request:', request.user)
    return  render(request,'home.html',{})

def about_view(request,*args, **kargs):
    #print('una request:', request.user)
    return  render(request,'about.html',{})

def contacts_view(request,*args, **kargs):
    return  render(request,'contacts.html',{})

