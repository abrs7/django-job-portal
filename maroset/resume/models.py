from django.db import models
from users.models import User
# Create your models here.


class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length=100)
    location = models.CharField(max_length = 256)
    job_title = models.CharField(max_length = 100)


    def __str__(self):
        return f'{self.first_name}{self.last_name}'
    
    

