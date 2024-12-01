from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.TextField()
    email = models.TextField()
    birth = models.DateTimeField()
    join_date = models.DateTimeField()