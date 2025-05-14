from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    isCompleted = models.BooleanField(default=False)
    