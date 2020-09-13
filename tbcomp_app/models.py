from django.db import models

# Create your models here.
class Student(models.Model):
    college = models.CharField(max_length = 50)
    year = models.CharField(max_length = 20)
    email = models.EmailField()
    fullname = models.CharField(max_length = 40, null=True)
    branch = models.CharField(max_length = 50, null=True)
    password = models.CharField(max_length = 20)
    confirmPassword = models.CharField(max_length = 20)
    question1=models.CharField(max_length = 20,null=True, blank=True)
    question2=models.CharField(max_length = 20,null=True, blank=True)
    question3=models.CharField(max_length = 20,null=True, blank=True)
    def __str__(self):
        return self.email

class Subject(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length = 60)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE, related_name = "Topic")

    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length = 20)
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE, related_name = "Activity")
    files = models.FileField(upload_to = 'activities', null = True, blank = True)
    driveLink=models.URLField(max_length=500)

    def __str__(self):
        return self.name+"_"+self.topic.name

class Document(models.Model):
    name = models.CharField(max_length = 60)
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE, related_name = "Document")
    files = models.FileField(upload_to = 'files', null = True, blank = True)

    def __str__(self):
        return self.name+"_"+self.topic.name

class StudentUpload(models.Model):
    STUDENT_UPLOAD_STATUS=(
        ('Approved','Approved'),
        ('Uploaded','Uploaded'),
        ('Rejected','Rejected'),
    )
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE, related_name = "StudentUpload")
    student = models.ForeignKey(Student, on_delete = models.CASCADE, related_name = "StudentUpload")
    files = models.FileField(upload_to = 'uploads', null = True, blank = True)
    status = models.CharField(max_length = 20, choices = STUDENT_UPLOAD_STATUS)
    name = models.CharField(max_length = 60)

    def __str__(self):
        return self.student.fullname+"_"+self.activity.topic.name+"_"+self.activity.name