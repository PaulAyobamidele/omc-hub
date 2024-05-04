from django.urls import path
from .views import UserLogout

urlpatterns = [
    path("logout/", UserLogout.as_view(), name="user-logout"),
]
