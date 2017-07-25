from django.contrib import admin
from .models import Student
from .models import Workers

# Register your models here.
# from challenge.models import Student
admin.site.register(Student)
admin.site.register(Workers)


