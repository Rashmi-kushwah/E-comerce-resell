from django.db import models

# Create your models here.
import uuid

class User(models.Model):

    Name = models.CharField(max_length=15)
    user_uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    Created_date = models.DateField(auto_now_add=True)
    otp = models.CharField(blank=True,null=True, max_length=20)
    profile_image_url = models.URLField(blank=True,null=True) 