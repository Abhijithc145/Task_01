from django.shortcuts import render,redirect
import os
from django.contrib import messages

from common.helpers.helper import permissions
from .form import *
from django.contrib import auth

# Create your views here.



        
def login(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login Successfully')
                return permissions(user.roles)
            else:
                messages.error(request, 'Invalid Credentials')
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')
    except Exception as Error:
        return render(request, 'login.html')


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
    if request.user.roles == "student":
        return render(request,'student.html')
    else:
        return redirect('logout')
        
def staffhome(request):
    if request.user.roles == "staff":
        return render(request,'staff.html')
    else:
        return redirect('logout')
    
def editorhome(request):
    try:
        if request.user.roles == "editor":
            return render(request,'editor.html')
        else:
            return redirect('logout')
    except Exception as Error:
        print("Error--->",Error)
        
def adminhome(request):
    if request.user.roles == "admin":
        return render(request,'admin.html')
    else:
        return redirect('logout')

def logout(request):
    auth.logout(request)
    messages.success(request, 'You are now Loged Out')
    return redirect('login')

