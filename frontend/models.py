from django.db import models
class UserCredentials(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128, unique=True)
    notes = models.TextField(max_length=1000)  # New field

    def __str__(self):
        return self.password
