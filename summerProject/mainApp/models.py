from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
# Create your models here.
class userInfo(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username
