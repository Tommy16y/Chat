from django.urls import path
from accounts.views import *



urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='user_registration'),
    path('verify/', VerifyCodeView.as_view(), name='verify_code'),
    path('agree/',AgreementView.as_view()),
    path('captcha/',register),
]