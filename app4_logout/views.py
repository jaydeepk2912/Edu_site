from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')
