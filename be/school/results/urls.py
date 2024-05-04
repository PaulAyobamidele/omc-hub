# urls.py

from django.urls import path, include
from rest_framework import routers
from .views import ResultViewSet, AuthTokenViewSet, StudentResultDownloadView

router = routers.DefaultRouter()
router.register(r"results", ResultViewSet)
router.register(r"auth-tokens", AuthTokenViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "download-result/", StudentResultDownloadView.as_view(), name="download-result"
    ),
]
