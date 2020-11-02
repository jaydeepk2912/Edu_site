from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import redirect
# Create your views here.
def login(request):
    if request.method=="POST":
        username_login=request.POST['username']
        password_login=request.POST['password']

        user=auth.authenticate(username=username_login,password=password_login)
        if user is None:
            #unsuccessfull go back
            return redirect('login')
        else:
            #log in successfully done go in..
            # '/' means home page
            auth.login(request, user)
            return redirect('/')
    else:
#get request
        return render(request,'login.html')


