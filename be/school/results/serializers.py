# serializers.py

from rest_framework import serializers
from .models import Result, AuthToken, Family, Student
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
        ]


class FamilySerializer(serializers.ModelSerializer):
    parent = UserSerializer()  # Serialize the parent user object

    class Meta:
        model = Family
        fields = ["id", "parent"]


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = [
            "id",
            "user",
            "family",
        ]


class ResultSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = Result
        fields = ["id", "student", "pdf", "uploaded_at"]


class AuthTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthToken
        fields = ["user", "token"]
