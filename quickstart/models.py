from django.contrib.auth.models import User
from django.db import models


class Social(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    portfolio = models.CharField(max_length=100)

    def __str__(self):
        return self.userid.username


