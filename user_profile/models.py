from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    mobile = models.CharField(max_length=10)
    profile_picture = models.ImageField(default=None, null=True, blank=True)
    
    def __str__(self):
        return str(self.user)