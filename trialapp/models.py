from django.db import models

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    des=models.TextField()

class team(models.Model):
        name = models.CharField(max_length=250)
        img = models.ImageField(upload_to='pics')
        des = models.TextField()
