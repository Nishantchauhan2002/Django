from django.db import models

# Create your models here.
class CustomUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(upload_to='user_photos/')
    gender = models.CharField(max_length=10)
    degree = models.CharField(max_length=100)
    college = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField()
    password = models.CharField(max_length=100)  # Store hashed passwords in production!
    dob = models.DateField()

    def __str__(self):
        return self.first_name + " " + self.last_name
