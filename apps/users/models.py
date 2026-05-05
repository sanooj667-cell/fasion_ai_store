from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.users import manager

# Create your models here.

class User(AbstractUser):
    username = None
    
