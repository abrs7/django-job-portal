from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class User(AbstractUser):
    email = models.BooleanField(unique=True)
    is_admin = models.BooleanField(default=False)
    is_candidate = models.BooleanField(default=False)
    is_company = models.BooleanField(default= False)
    is_private_employer = models.BooleanField(default= False)
    has_resume = models.BooleanField(default=False)
    has_company = models.BooleanField(default=False)



    def is_admin_user(self):
        return self.is_admin
    def is_candidate_user(self):
        return self.is_candidate

    def is_company_user(self):
        return self.is_company

    def is_private_employer_user(self):
        return self.is_private_employer