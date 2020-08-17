from django.db import models

# Create your models here.
class Student(models.Model):
    college = models.CharField(max_length = 50)
    year = models.CharField(max_length = 20)
    email = models.EmailField()
    fullname = models.CharField(max_length = 30, null=True)
    branch = models.CharField(max_length = 10, null=True)
    password = models.CharField(max_length = 20)
    confirmPassword = models.CharField(max_length = 20)
    question1=models.CharField(max_length = 20,null=True, blank=True)
    question2=models.CharField(max_length = 20,null=True, blank=True)
    question3=models.CharField(max_length = 20,null=True, blank=True)
    def __str__(self):
        return self.email

class Subject(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length = 50)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE, related_name = "Topic")

    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length = 20)
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE, related_name = "Activity")
    files = models.FileField(upload_to = 'activities', null = True, blank = True)

    def __str__(self):
        return self.name

class Document(models.Model):
    name = models.CharField(max_length = 50)
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE, related_name = "Document")
    files = models.FileField(upload_to = 'files', null = True, blank = True)

    def __str__(self):
        return self.name

class StudentUpload(models.Model):
    STUDENT_UPLOAD_STATUS=(
        ('approved','approved'),
        ('uploaded','uploaded'),
    )
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE, related_name = "StudentUpload")
    student = models.ForeignKey(Student, on_delete = models.CASCADE, related_name = "StudentUpload")
    files = models.FileField(upload_to = 'uploads', null = True, blank = True)
    status = models.CharField(max_length = 20, choices = STUDENT_UPLOAD_STATUS)
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name
