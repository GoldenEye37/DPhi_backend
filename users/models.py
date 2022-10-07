import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


# Create your models here.
class UserType(models.TextChoices):
    # name = models.CharField(max_length=255, unique=True, null=False)
    educator = 'educator', _('educator')
    student = 'student', _('student')

    # User_type = [
    #     (educator, 'educator'),
    #     (user, 'user'),
    # ]


class User(AbstractUser):
    id = models.UUIDField(verbose_name=None, primary_key=True, default=uuid.uuid4, editable=False)
    email_address = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)  # inherit the django user
    first_name = models.CharField(blank=False, null=False, unique=False, max_length=255)
    last_name = models.CharField(blank=False, null=False, unique=False, max_length=255)
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    user_type = models.CharField(
        UserType, choices=UserType.choices, null=True, blank=True, on_delete=models.CASCADE, default=UserType.user
    )

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        ordering = ['user__first_name', 'user__last_name']
        verbose_name_plural = 'Profiles'
