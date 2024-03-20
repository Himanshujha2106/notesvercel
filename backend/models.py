from django.db import models
class UserCredentials(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=254)  # New field

    def __str__(self):
        return self.username
