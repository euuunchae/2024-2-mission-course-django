from django.db import models

# Create your models here.

class Member(models.Model):
    member_id = models.IntegerField(primary_key = True)
    name = models.TextField()
    email = models.TextField(unique=True)
    birth = models.DateField(null=True)
    join_date = models.DateField()