from django.db import models
from users.models import User

# Create your models here.
class PrivateRecruiter(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 100, null=True, blank=True)
    last_name = models.CharField(max_length =100, null=True, blank=True)
    city = models.CharField(max_length = 100, null=True, blank=True)
    state = models.CharField(max_length = 100, null=True, blank=True)

    def __str__(self):
        return self.first_name