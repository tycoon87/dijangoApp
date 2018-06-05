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
    Blog_id = Blog_id
    return request ('Blogapp/new.html',Blog_id)

def editblog (request, Blog_id):
    return redirect('/')

def delete (request, Blog_id):
    return redirect('/')