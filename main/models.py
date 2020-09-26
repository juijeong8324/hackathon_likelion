from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=20)
    email = models.TextField(max_length=100)
    
class Post(models.Model):
    title = models.TextField(max_length=100)
    pub_date = models.DateTimeField()
    department = models.TextField(max_length=20)
    content = models.TextField(max_length=500)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title