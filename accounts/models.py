from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
  bio = models.TextField(max_length=500)
  picture = models.TextField()
  creditcard = models.IntegerField(default=1,validators=[MaxValueValidator(1000000000),MinValueValidator(1)])

  def __str__(self):
    return self.user.username

