from django.db import models

class User(models.Model):
    name = models.CharField(max_length=25)
    passsword= models.CharField(max_length=30)
    surname = models.CharField(max_length=45)
    country = models.CharField(max_length=20)
    city= models.CharField( max_length=50)
    date_created = models.DateField(auto_now_add=True)

def __str__(self):
    return f'{self.name} {self.surname}'
