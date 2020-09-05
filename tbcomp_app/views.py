from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Student, Document, StudentUpload, Activity

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
            return redirect("subjects")
        else:
            messages.error(request, 'Input correct username and password')
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
        if Student.objects.filter(email=email,question1=question1,question2=question2,question3=question3).exists():
            password=Student.objects.get(email=email).password
            user = authenticate(request, username = email, password = password)
            auth.login(request,user)
            return redirect("resetPassword")
        else:
            messages.error(request, 'input correct email or answers')
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
            return redirect("resetPassword")
    template_name = 'resetPassword.html'
    return render(request, template_name)


@login_required(login_url="login")
def subjects(request):
    context={'student':Student.objects.get(email=request.user.username)}
    return render(request, 'subjects.html',context)


@login_required(login_url="login")
def documents(request,subject,topic):
    if(subject=="EEEE"):
        template_name=str(topic)+".html"
        context={'subject':subject,'topic':topic,'student':Student.objects.get(email=request.user.username)}
        return render(request,template_name,context)
    else:
        if request.method == "POST" and request.FILES['file-upload-input-doc1']:
            email = request.user.username
            studentUploads = StudentUpload.objects.filter(student__email__contains = email, activity__topic__name__contains = topic, activity__topic__subject__name__contains = subject)
            activity_name=request.POST["activity_name"]
            act = Activity.objects.get(name = activity_name, topic__name__contains = topic, topic__subject__name__contains = subject)
            stu = Student.objects.get(email = email)
            if(not(StudentUpload.objects.filter(student__email__contains = email, activity__name__contains = activity_name, activity__topic__name__contains = topic, activity__topic__subject__name__contains = subject).exists())):
                new = StudentUpload.objects.create(
                    student = stu,
                    status = 'Uploaded',
                    activity = act,
                )
                new.save()
                new.files = request.FILES['file-upload-input-doc1']
                new.name = request.FILES['file-upload-input-doc1'].name
                new.save()
        email = request.user.username
        
        studentUploads = StudentUpload.objects.filter(student__email__contains = email, activity__topic__name__contains = topic, activity__topic__subject__name__contains = subject)
        message=""
        if(StudentUpload.objects.filter(student__email__contains = email, activity__topic__name__contains = topic, activity__topic__subject__name__contains = subject, status="Rejected").exists()):
            message="Your previous activity was rejected. Please upload a different one."
        StudentUpload.objects.filter(student__email__contains = email, activity__topic__name__contains = topic, activity__topic__subject__name__contains = subject, status="Rejected").delete()
        documents_list_names=["doc1","doc2","doc3"]
        activity_questions_list_names=["activity_1"]
        documents=[]
        activities=[]
        for u in studentUploads:
            if u.activity.name == "activity_1":
                if u.status == "Approved":
                    documents_list_names+=["doc4","doc5","doc6"]
                    activity_questions_list_names+=["activity_2"]
            else:
                if u.status == "Approved":
                    documents_list_names+=["doc7","doc8","doc9"]
        for i in documents_list_names:
            documents+=Document.objects.filter(name= i , topic__name__contains = topic, topic__subject__name__contains = subject)
        for j in activity_questions_list_names:
            activities+=Activity.objects.filter(name= j , topic__name__contains = topic, topic__subject__name__contains = subject)
        template_name = 'documents.html'
        context={'subject':subject,'topic':topic, 'documents' : documents, 'activities' : activities, 'uploads' : studentUploads, 'message':message,'student':Student.objects.get(email=request.user.username)}
        return render(request,template_name,context)

def aboutus(request):
    return render(request,'aboutus.html')

