from django.shortcuts import render, HttpResponse, redirect
# from .models import User
from django.contrib import messages
# Create your views here.

def index (request):
    return render(request,'Blogapp/index.html')

def new (request):
    return render(request,'Blogapp/new.html')
    
def create (request):
    return render(redirect,'/')

def show (request, Blog_id):
    contents = {
        'id':Blog_id
    }
    print 
    return render(request,'Blogapp/new.html', contents)

def editblog (request, Blog_id):
    return redirect('/')

def delete (request, Blog_id):
    return redirect('/')