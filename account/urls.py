# account/urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserViewSet, CustomUserCreate

urlpatterns = [
    # Paths for JWT authentication
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', CustomUserCreate.as_view(), name='create_user'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
