
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

# Create your models here.
from Users.managers import CustomUserManager


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    isbusiness = models.BooleanField(default=False)


    REQUIRED_FIELDS = ['isbusiness']
    USERNAME_FIELD = 'username'

    class Meta:
        ordering=['id']

    objects = CustomUserManager()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    #if user obj is created and saved in db
    if created:
        Token.objects.create(user=instance)
