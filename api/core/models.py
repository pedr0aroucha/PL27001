from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    city = models.CharField(max_length=100)
    description = models.TextField()
    phone = models.CharField(max_length=11, null=True)
    email = models.EmailField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    end_date = models.DateTimeField(null=True, blank=True)
    begin_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='book', blank=True, null=True)
    
