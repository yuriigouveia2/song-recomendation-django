from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    birth = models.DateField()
    created_at = models.DateField(auto_now_add=True)

class CustomUser(AbstractUser):
    # Create custom fields
    pass