# models.py

from django.db import models
from django.contrib.auth.models import User


class Family(models.Model):
    parent = models.OneToOneField(User, on_delete=models.CASCADE, related_name="family")
    # Add any other fields related to the family/parent account here


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student")
    family = models.ForeignKey(
        Family, on_delete=models.CASCADE, related_name="students"
    )
    # Add any other fields related to the student account here


class Result(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="results"
    )
    pdf = models.FileField(upload_to="results/")
    uploaded_at = models.DateTimeField(auto_now_add=True)


class AuthToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=50)
