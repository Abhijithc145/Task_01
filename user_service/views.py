from django.shortcuts import render,redirect
import os
from django.contrib import messages
from .form import *
from django.contrib import auth

# Create your views here.
def login(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            print(username,"     ----    ",password)
            print("user-->",user)
            if user is not None:
                auth.login(request, user)
                print("user--->",user.roles)
                messages.success(request, 'Login Successfully')
                return redirect('studenthome')
            else:
                messages.error(request, 'Invalid Credentials')
                return render(request, 'login.html')

        else:
            return render(request, 'login.html')
    except Exception as Error:
        print("Error--->",Error)
        pass


def signup(request):
    form = signupform(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
                user = form.save(commit=False)
                user.set_password(request.POST['password'])  # Use set_password to set the user's password
                user.save()
                return redirect('login')          
        return render(request, 'signup.html',{'err': "number doesn't exist",'form': form})
    return render(request, 'signup.html',{'form':form})


def studenthome(request):
    return render(request,'student.html')

def logout(request):
    auth.logout(request)
    messages.success(request, 'You are now Loged Out')
    return redirect('login')