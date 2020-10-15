from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

def handleSignup(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        if len(uname)>10:
            messages.warning(request, "Username should be less than 10 characters")
            return redirect('/')

        if not uname.isalnum():
            messages.warning(request, "Username should contain only letter and numbers")
            return redirect('/')

        if pass1 != pass2:
            messages.warning(request, "Password do not match")
            return redirect('/')

        try:
            if User.objects.get(uname= uname):
                messages.warning(request, "Username already taken")
                return redirect('/')
        
        except Exception as identifier:
            pass

        myuser = User.objects.create_user(uname, email, pass1)
        myuser.save()
        messages.success(request, "Signup Successful Please Login")
        return redirect('/')
    return render(request, 'index.html')

def handleLogin(request):
    if request.method == "POST":
        loginusername = request.POST("uname")
        loginpassword = request.POST('pass1')
        user = authenticate(uname = loginusername, pass1 = loginpassword)
        if user is not None:
            login(request, user)
            messages.info(request,"Login Success")
            return redirect('/')
        else:
            messages.warning(request, "Invalid Credentials")
            return redirect('/')
    return render(request, 'index.html')