from django.db import models
from users.models import User

# Create your models here.
class Admin(models.model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    role = models.CharField(max_length = 100)

    def __str__(self):
        return self.name