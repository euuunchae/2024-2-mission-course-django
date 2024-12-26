from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=10)
    email = models.TextField(unique=True)
    birth = models.DateField(null=True)
    join_date = models.DateField(auto_now_add=True)
