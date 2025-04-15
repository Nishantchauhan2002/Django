from django.db import models
from django.utils import timezone

# Create your models here.
class userData(models.Model):
    USER_TYPE = [
        ('st','student'),
        ('wd','warden'),
        ('pt','parents'),
        ('gt','guests')
    ]
    firstName = models.CharField(max_length=50)
    image = models.ImageField(upload_to='users/')
    date_added = models.DateTimeField(default = timezone.now, auto_now=False, auto_now_add=False)
    type = models.CharField(max_length=2,choices = USER_TYPE)
    
    def __str__(self):
        return self.firstName
    

 