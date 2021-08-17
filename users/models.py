
from django.contrib.auth.models import User
from django.db import models


class profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=200)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=10, blank=True)

    picture = models.ImageField(
        upload_to='users/picture', blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username

