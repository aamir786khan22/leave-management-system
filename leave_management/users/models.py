from django.db import models
import uuid
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    ROLE_CHOICES = [('Admin', 'Admin'), ('Employee', 'Employee')]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Employee')
    email_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=100, blank=True, null=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def generate_verification_token(self):
        token = str(uuid.uuid4())
        self.verification_token = token
        self.save()
        return token

    def __str__(self):
        return self.email
