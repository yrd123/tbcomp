from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Student

# Create your views here.
def index(request):
    return render(request,'index.html')

def loguser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            print('User verified')
            print(request.user.username)
            return redirect("subject")
        else:
            messages.error(request, 'Input correct username and password')
            print('No such user')
    template_name = 'login.html'
    return render(request, template_name)

def logoutUser(request):
    logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if Student.objects.filter(email = email).exists():
            messages.error(request, 'Email already taken. Try a different one.')
        else:
            obj1 = User.objects.create(
                username = email,
                email = email,
            )
            obj1.set_password(request.POST.get('password'))
            obj1.save()
            year = request.POST.get('year')
            college = request.POST.get('college')
            password = request.POST.get('password')
            confirmpassword = request.POST.get('confirmPassword')
            obj2 = Student.objects.create(
                email = email,
                year = year,
                college = college,
                password = password,
                confirmPassword = confirmpassword,
            )
            obj2.save()
            return redirect("login")
    template_name = 'signup.html'
    return render(request, template_name)

def resetPassword(request):
    template_name = 'ResetPassword.html'
    return render(request, template_name)