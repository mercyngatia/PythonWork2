from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
from .models import datetime
from .models import Worker


# Create your views here.
def welcome(request):
    return render(request, 'welcome_page.html')

# def Welcome(request):
#     return render(request,'Welcome-studets.html')
def Students(request):
    students=Student.objects.all()
    context = {
              'student':students
    }
    return render(request,'welcome_page.html',context)
    
    
# def Worker(request):
#     workers=Workers.objects.all()
#     context = {
#               'workers':workers
#     }
#     return render(request,'welcome_page.html',context)