from django.db import models
from django.contrib.auth.models import User

class UserExtension(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  descripcion = models.CharField(max_length=255, null=True, blank=True)
  link = models.URLField(null=True, max_length=100)
  avatar = models.ImageField(null=True, upload_to='avatares', blank=True)
  
  def __str__(self):
    return self.user.username