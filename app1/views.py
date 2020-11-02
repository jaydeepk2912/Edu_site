from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'a.html',{'titles':'Django','link':'https://www.w3schools.com'})

'''
def profile(request):
    return HttpResponse("profile page")    
'''

def profile(request):
    return render(request,'a.html',{'titles':'profile page','link':"http://127.0.0.1:8000/"})


def expression(request):
    a=int(request.POST['text1'])
    b=int(request.POST['text2'])
    c=a+b
    return render(request,'output.html',{'result':c})