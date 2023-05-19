from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.account.managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)