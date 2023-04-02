from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from twilio.rest import Client
from rest_framework import serializers
from .models import CustomUser,Agreement

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # verification_code = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('phone_number', 'username', 'password','agreement')
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate_agreement(self, value):
        # if value !='да' or 'Да':
        if not value:
            raise serializers.ValidationError('Вы должны принять правила пользованием приложением')
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        # verification_code = validated_data.pop('verification_code')
        user = CustomUser(**validated_data)
        user.set_password(password)
        # user.is_active = True
        user.save()
        return user

 




class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = '__all__'