from datetime import datetime
import email
from turtle import title
from typing_extensions import Required
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    auther = models.CharField(max_length=100)
    email = models.EmailField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
