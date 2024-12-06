from django.urls import path
from . import views
# salim/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views

from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.homepage , name='homepage'),
    path('contact/', views.contact, name='contact'),

    path('about/', views.about, name='about'),
    path('trainers/', views.trainers, name='trainers'),
    path('events/', views.events, name='events'),

    path('ict_department/', views.ict_department, name='ict_department'),
    path('electrical_department/', views.electrical_department, name='electrical_department'),
    path('fashion_department/', views.fashion_department, name='fashion_department'),
    path('hairdressing_department/', views.hairdressing_department, name='hairdressing_department'),
    path('finance_department/', views.finance_department, name='finance_department'),
    path('library_department/', views.library_department, name='library_department'),
    path('examination_department/', views.examination_department, name='examination_department'),
path('lms/', views.lms, name='lms'),


    path('courses/', views.courses, name='courses'),
]



