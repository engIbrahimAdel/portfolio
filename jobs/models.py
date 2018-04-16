from django.db import models

# Create your models here.
#models mainly is a classes
class job(models.Model):
    #image
    image=models.ImageField(upload_to='images/')
    #text
    summary=models.CharField(max_length=200)
