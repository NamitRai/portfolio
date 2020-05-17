from django.db import models

# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    image = models.ImageField(upload_to="images/")
    summary = models.TextField(max_length=400)

    def __str__(self):
        return self.name

    def sum(self):
        return self.summary[:100]

    def pub_date(self):
        return self.date.strftime('%b %e %Y')
