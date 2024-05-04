from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Result, AuthToken
from .serializers import ResultSerializer, AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Assign the current user (school administration) to the result
        serializer.save(student=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class AuthTokenViewSet(viewsets.ModelViewSet):
    queryset = AuthToken.objects.all()
    serializer_class = AuthTokenSerializer

    @action(detail=False, methods=["post"])
    def generate_token(self, request):
        user = request.user
        # Check if the user already has a token
        if AuthToken.objects.filter(user=user).exists():
            token_instance = AuthToken.objects.get(user=user)
            serializer = self.get_serializer(token_instance)
            return Response(serializer.data)
        # Generate a new token
        token_instance = AuthToken.objects.create(user=user)
        serializer = self.get_serializer(token_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["get"])
    def my_token(self, request):
        user = request.user
        # Retrieve the token associated with the current user
        token_instance = get_object_or_404(AuthToken, user=user)
        serializer = self.get_serializer(token_instance)
        return Response(serializer.data)


class StudentResultDownloadView(generics.RetrieveAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        result = self.get_object()
        file_path = result.pdf.path
        with open(file_path, "rb") as f:
            response = HttpResponse(f.read(), content_type="application/pdf")
            response["Content-Disposition"] = "inline; filename=" + result.pdf.name
            return response
