from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as auth_login
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
def home(request):
    return render(request,'index.html')
def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        s=authenticate(username=username,password=password)
        if s is not None:
            auth_login(request,s)
            return redirect('project')
        else:
            # return HttpResponse("Please enter valid details")
            messages.error(request, 'Please enter details')
    else:
        return render(request,'login.html')
def register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        mobnumber=request.POST.get("mobnumber")
        password=request.POST.get("password")
        if email and username and password and mobnumber:
                c=User.objects.create_user(username=username,email=email,password=password)
                c.save()
                return redirect("login")
        else:
            messages.error(request, 'Please fill in all required fields')
    else:
        return render(request,"register.html")
    return render(request,'register.html')
def project(request):
    return render(request,'project.html')
def menu(request):
    return render(request,'menu.html')
def table(request):
    return render(request,'table.html')