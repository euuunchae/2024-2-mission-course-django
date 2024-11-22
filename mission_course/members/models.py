from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.TextField()
    email = models.TextField()
    birth = models.DateField()
    join_date = models.DateField()