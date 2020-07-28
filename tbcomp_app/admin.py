from django.contrib import admin
from .models import Student
from .models import Subject
from .models import Topic
from .models import Activity
from .models import Document
from .models import StudentUpload

# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(Activity)
admin.site.register(Document)
admin.site.register(StudentUpload)

