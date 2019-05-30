from django.db import models
from django.contrib.auth.models import User
#from hike.models import Hike, Comments, HikeGroup

# Create your models here.

class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
  bio = models.TextField(max_length=500)
  picture = models.TextField()

  def __str__(self):
    return self.user.username

