from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from .models import Student

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('emailId')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            print('User verified')
            print(request.user.username)
            return redirect("subject")
        else:
            messages.error(request, 'Input correct username and password')
            print('No such user')
    template_name = 'login.html'
    return render(request, template_name)

def logout(request):
    auth.logout(request)
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
            question1=request.POST.get("question1")
            question2=request.POST.get("question2")
            question3=request.POST.get("question3")
            obj2 = Student.objects.create(
                email = email,
                year = year,
                college = college,
                password = password,
                confirmPassword = confirmpassword,
                question1=question1,
                question2=question2,
                question3=question3
            )
            obj2.save()
            return redirect("login")
    template_name = 'signup.html'
    return render(request, template_name)

def resetPasswordQuestions(request):
    if request.method=="POST":
        email=request.POST.get("emailId")
        question1=request.POST.get("question1")
        question2=request.POST.get("question2")
        question3=request.POST.get("question3")
        print(question1,question2)
        if Student.objects.filter(email=email,question1=question1,question2=question2,question3=question3).exists():
            print("inside q")
            password=Student.objects.get(email=email).password
            print(password)
            user = authenticate(request, username = email, password = password)
            auth.login(request,user)
            return redirect("resetPassword")
        else:
            messages.error(request, 'input correct email or answers')
            print('incorrect answers or email')
    template_name = 'resetPasswordQuestions.html'
    return render(request, template_name)

@login_required(login_url="login")
def resetPassword(request):
    if request.method=="POST":
        return redirect("subject")
    print("inside resetpassword: ",request.user.username)
    template_name = 'resetPassword.html'
    return render(request, template_name)