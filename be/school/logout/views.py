from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import logout
from rest_framework import status


class UserLogout(APIView):
    def post(self, request):
        auth_token = request.headers.get("Authorization")

        if auth_token:
            auth_token = auth_token.split(" ")[1]

            try:
                token = Token.objects.get(key=auth_token)
            except Token.DoesNotExist:
                return Response(
                    {"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED
                )

            token.delete()

            logout(request)

            return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)

        return Response(
            {"error": "Authorization header with token is required"},
            status=status.HTTP_400_BAD_REQUEST,
        )


# 7f09947449333bacbf6bd76aca1de26da84f2008
