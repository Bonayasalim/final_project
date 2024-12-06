from urllib import request

from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import LearnerRegistrationForm, ApplicationForm
from .models import Course, Application
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import login
from django.shortcuts import render


def homepage(request):
    return render (request, 'part/index.html')
def contact(request):
    return render (request, 'part/contact.html')
def courses(request, form=None):
    return render(request, 'part/courses.html', {'form': form})
def about(request):
    return render(request, 'part/about.html')
def trainers(request):
    return render (request, 'part/trainers.html')
def events(request):
    return render (request, 'part/events.html')

def ict_department (request):
    return render (request, 'part/ict_department.html')
def electrical_department (request):
    return render(request, 'part/electrical_department.html')
def fashion_department (request):
    return render (request, 'part/fashion_department.html')
def hairdressing_department (request):
    return render (request, 'part/hairdressing_department.html')
def finance_department (request):
    return render (request, 'part/finance_department.html')
def library_department (request):
    return render (request, 'part/library.html')
def examination_department (request):
    return render (request, 'part/examination_department.html')
def lms (request):
    return render (request, 'part/lms.html')





