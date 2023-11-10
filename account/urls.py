from django.urls import path
from .views import UserRegister, UserVerification
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('', views.getroutes, name='getroutes'),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', UserRegister.as_view(), name='signup'),
    path('signup/get_otp/<int:userid>/', UserVerification.as_view(), name='get_otp'),
   # path('signup/otp/<int:userid>/<int:otp>/', UserVerification.as_view(), name='verify'),
]