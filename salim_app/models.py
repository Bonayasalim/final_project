
from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    CATEGORY_CHOICES = [
        ('EEE', 'Electrical and Electronic Engineering'),
        ('FD', 'Fashion Design'),
        ('HB', 'Hairdressing and Beauty'),
        ('ICT', 'Information Communication Technology'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    description = models.TextField()
    duration = models.CharField(max_length=50)  # Example: "1 Year"

    def __str__(self):
        return self.name

class Application(models.Model):
    learner = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.learner.username} - {self.course.name}"


class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course_preference = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

