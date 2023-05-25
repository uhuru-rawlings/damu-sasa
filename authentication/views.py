from django.shortcuts import render, redirect
from .models import Registration
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime

# Create your views here.
def loginView(request):
    error = ""
    if request.method == "POST":
        Email = request.POST['username']
        Password = request.POST['password']
        
        login_user = Registration.objects.filter(Email = Email)
        if login_user.exists():
            login_user = Registration.objects.get(Email = Email)
            if check_password(Password, login_user.Password):
                login_user.LastLogin = datetime.now()
                login_user.save()
                
                respose =  redirect('dashboard')
                respose.set_cookie("useremail", login_user.Email)
                return respose
            else:
                error = "Oops! wrong password try again"
        else:
            error = "Oops! user with these credentials dont exist"
            
    context = {
        'title' : 'Login User',
        'error': error
    }
    return render(request, 'login.html', context)

def signupView(request):
    error = ""
    if request.method == "POST":
        Fullname = request.POST['fullname']
        Email = request.POST['username']
        Password = request.POST['password']
        
        
        login_user = Registration.objects.filter(Email = Email)
        if login_user.exists():
                error = "Oops! user with these credentials already exist"
        else:
           new_user = Registration(
               Fullname  = Fullname,
               Email  = Email,
               Password  = make_password(Password)
           )
           new_user.save()
           
           return redirect("login")
       
    context = {
        'title' : 'Create Account',
        'error': error
    }
    return render(request, 'signup.html', context)

def resetView(request):
    error = ""
    if request.method == "POST":
        Email = request.POST['username']
        Password = request.POST['password']
        
        login_user = Registration.objects.filter(Email = Email)
        if login_user.exists():
            login_user = Registration.objects.get(Email = Email)
            login_user.Password = make_password(Password)
            login_user.save()
            
            return redirect('login')
        else:
            error = "Oops! user with these credentials dont exist"
        
    context = {
        'title' : 'Reset Password',
        'error': error
    }
    return render(request, 'reset.html', context)