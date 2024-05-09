from django.db import models
from user.models import User
import uuid
from django.utils import timezone

class Product(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user =models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=255,blank=False)
    rate=models.IntegerField(blank=True,null=True)
    description=models.CharField(max_length=699,blank=False)
    category=models.CharField(max_length=255,blank=False)
    total=models.IntegerField(blank=False)
    stack=models.IntegerField(blank=False)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
   