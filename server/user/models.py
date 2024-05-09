from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

import uuid

class User(AbstractUser):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255,unique=True)
    password = models.CharField(max_length=128)
    username = None
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    
    