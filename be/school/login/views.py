from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status


class UserLogin(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                # Retrieve or create a token for the authenticated user
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )
