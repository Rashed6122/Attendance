from django.db import models

# Create your models here.
class image(models.Model):
    Img = models.ImageField(upload_to='uploads/')
    