from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.views import APIView
from messagebird.client import ErrorException
from rest_framework import generics
from .serializers import UserSerializer
from .models import CustomUser
from twilio.rest import Client
from django.conf import settings
from django.http import JsonResponse
from phonenumbers import parse, is_valid_number
from accounts.forms import UserRegistrationForm
import random
from django.views.generic import TemplateView
from .models import Agreement
from .serializers import AgreementSerializer
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from django.views.decorators.csrf import csrf_exempt

from captcha.fields import CaptchaStore

User = get_user_model()





def generate_verification_code():
    return str(random.randint(1000, 9999))


class UserRegisterAPIView(APIView):
    # template_name = 'registration.html'
    def post(self, request):
        data = request.data.copy()

        # Validate phone number format
        phone_number = data.get('phone_number')
        if phone_number:
            try:
                phone_number = parse(phone_number)
                if not is_valid_number(phone_number):
                    return JsonResponse({'error': 'Неверный формат номера телефона'}, status=status.HTTP_400_BAD_REQUEST)
                data['phone_number'] = phone_number.national_number
            except:
                return JsonResponse({'error': 'Неверный формат номера телефона'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'error': 'Телефон уже есть'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            verification_code = generate_verification_code()
            print(verification_code)
            # user.save(verification_code=verification_code)
    
            client = Client('ТУТ ID ДОЛЖНО БЫТЬ ОТ ТВИЛИО', 'ID ОТ ТВИЛИО 2')
            message = client.messages.create(
                body=f"Your verification code is {verification_code}",
                from_= +15856696793,
                to=f"+{phone_number.country_code}{phone_number.national_number}"
            )

            # Save user with verification code
            user = serializer.save(verification_code=verification_code)
            user.verification_code=verification_code
            user.agreement = True

            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def form_valid(self, form):
    #     # Verify captcha
    #     captcha_view = CaptchaView.as_view()
    #     captcha_response = captcha_view(self.request).content.decode('utf-8')
    #     if captcha_response == 'False':
    #         form.add_error(None, 'Invalid captcha. Please try again.')
    #         return super().form_invalid(form)

    #     # Save user data
    #     form.save()

    #     return super().form_valid(form)


class VerifyCodeView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        verification_code = request.data.get('verification_code')

        try:
            user = CustomUser.objects.get(phone_number=phone_number, verification_code=verification_code)
            user.is_active = True
            user.save()
            return JsonResponse({'success': 'Вы успешно зарегистрировались'}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return JsonResponse({'error': 'Код неверный'}, status=status.HTTP_400_BAD_REQUEST)



from django.shortcuts import render

# class CaptchaView(TemplateView):   
#     template_name = 'registration.html' 
    
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            p=phone_number
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create_user(phone_number=phone_number,username=username, password=password,agreement = True)
            # if p == User.objects.get(phone_number=phone_number).phone_number: 
            #     user = User.objects.get(phone_number=phone_number)
            #     verification_code = generate_verification_code()
            #     p = phone_number
            #     print(verification_code)
                # user.save(verification_code=verification_code)
                # client = Client('AC8f8a230be0ac360c170fb81eba74673e', 'c11104cde487302c517d53d7a195d624')
                # message = client.messages.create(
                #     body=f"Your verification code is {verification_code}",
                #     from_= +15856696793,
                #     to=f"+{phone_number.country_code}{phone_number.national_number}"
                # 
                # client = Client('AC8f8a230be0ac360c170fb81eba74673e', 'c11104cde487302c517d53d7a195d624')
                # message = client.messages.create(
                #     body=f"Your verification code is {verification_code}",
                #     from_= +15856696793,
                #     to = +996770810003,
                # )
                # user = serializer.save(verification_code=verification_code)
                # user.verification_code=verification_code  
            return render(request, 'registration_success.html')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             phone_number = form.cleaned_data['phone_number']
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             User.objects.create_user(phone_number=phone_number,username=username, password=password)
#             return render(request, 'registration_success.html')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'registration.html', {'form': form})



class AgreementView(APIView):
    def get(self, request):
        agreement = Agreement.objects.order_by('-date_created').first()
        serializer = AgreementSerializer(agreement)
        return Response(serializer.data)

