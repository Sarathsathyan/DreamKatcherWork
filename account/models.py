from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserMore(models.Model):
    u_id = models.ForeignKey(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.phone