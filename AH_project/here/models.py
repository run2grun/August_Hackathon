from django.db import models

# Create your models here.
class Text(models.Model):
    title=models.CharField(max_length=50,null=True)
    name=models.CharField(max_length=50,null=True)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text

class Movie(models.Model):
    title=models.CharField(max_length=50,null=True)
    text=models.TextField()

    def __str__(self):
        return self.title