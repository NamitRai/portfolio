from django.db import models

# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    image = models.ImageField(upload_to="images/")
    summary = models.TextField(max_length=400)
