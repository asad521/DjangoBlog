from django.db import models

# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=150, default="Some String")
    desc = models.TextField()