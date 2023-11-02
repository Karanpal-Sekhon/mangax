from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.id, filename)


class User(AbstractUser):

    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=100)

    image = models.ImageField(upload_to=user_directory_path, default= "vendor.jpg")
    description = models.TextField(null=True, blank=True, default="Vendor Description")

    authentic_rating = models.CharField(max_length=100, default = "100")


    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):

        return self.username
