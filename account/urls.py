from django.urls import path
from .views import UserRegister, UserVerification
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('signup/', UserRegister.as_view(), name='signup'),
    path('signup/get_otp/<int:userid>/', UserVerification.as_view(), name='get_otp'),
   # path('signup/otp/<int:userid>/<int:otp>/', UserVerification.as_view(), name='verify'),
]