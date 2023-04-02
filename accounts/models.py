from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model


class UserManager(BaseUserManager):
    def create_user(self, phone_number, username, password=None, **extra_fields):
        if not phone_number:
            raise ValueError(_('The Phone Number field must be set'))
        user = self.model(
            phone_number=phone_number,
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user_admin(self, username, password=None, **extra_fields):
        user = self.model(
            username=username,
            **extra_fields
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user_admin(username, password, **extra_fields)

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)

    username = models.CharField(_('username'), max_length=30, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    about = models.TextField(_('about'), blank=True)
    profile_picture = models.ImageField(_('profile picture'), upload_to='profile_pictures/', blank=True)
    is_active = models.BooleanField(_('active'), default=False)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    verification_code = models.CharField(_('verification code'), max_length=6, blank=True)
    agreement = models.BooleanField(default=False)
    objects = UserManager()


    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.username
    


User = get_user_model()



class Agreement(models.Model):
    # id = models.AutoField(primary_key=True)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)


    # def __str__(self):
        # return f"Agreement {self.id}"
