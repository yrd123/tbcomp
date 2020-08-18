from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Student, Document, StudentUpload


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
            return redirect("subjects")
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
            fullname = request.POST.get('fullname')
            branch = request.POST.get('branch')
            year = request.POST.get('year')
            college = request.POST.get('college')
            password = request.POST.get('password')
            confirmpassword = request.POST.get('confirmPassword')
            question1=request.POST.get("question1")
            question2=request.POST.get("question2")
            question3=request.POST.get("question3")
            obj2 = Student.objects.create(
                email = email,
                fullname=fullname,
                branch=branch,
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
        email=request.POST.get("emailId")
        Resetpassword=request.POST.get("Resetpassword")
        confirmPassword=request.POST.get("confirmPassword")
        if Student.objects.filter(email=email).exists():
            obj3=User.objects.get(email=email)
            obj3.set_password(Resetpassword)
            obj3.save()
            Student.objects.filter(email=email).update(password=Resetpassword, confirmPassword=confirmPassword)
            return redirect("subject")
        else:
            messages.error(request, 'Input correct email id')
            print('incorrect email')
            return redirect("resetPassword")
    template_name = 'resetPassword.html'
    return render(request, template_name)

@login_required(login_url="login")
def documents(request,subject,topic):
    # studentUploads=StudentUpload.objects.filter(student__email__contains=request.user.username)
    # documents_list_names=["document_1","document_2","document_3"]
    # activity_questions_list_names=["activity_1"]
    # uploaded_activities_list=[]
    # if studentUploads.objects.filter(name="uploaded_activity_1").exists():
    #     uploaded_activities_list+=["activity_1_solution"]
    #     if studentUploads.objects.filter(name="uploaded_axtivity_1").status=="approved":
    #         documents_list_names+=["document_4","document_5","document_6"]
    #         activity_questions_list_names+=["activity_2"]
    #         if studentUploads.objects.filter(name="uploaded_activity_2").exists():
    #             uploaded_activities_list=["activity_2_solution"]
    #             if studentUploads.objects.filter(name="uploaded_activity_2").status=="approved":
    #                 documents_list_names+=["document_7","document_8","document_9"]
    # documents=Document.objects.filter(topic__name__contains=topic,name=documents_list_names).order_by("name").files
    # activities=Activity.objects.filter(topic__name__contains=topic,name=activity_questions_list_names).order_by("name").files
    print("subject:",subject)
    print("topic:",topic)
    return render(request,"documents.html")


@login_required(login_url="login")
def subjects(request):
    return render(request, 'subjects.html')
