from django.db import models

# Create your models here.

class UserRegister(models.Model):
    u_name=models.CharField(max_length=100)
    u_phone=models.CharField(max_length=100,unique=True)
    u_email=models.EmailField(unique=True)
    u_pass=models.CharField(max_length=100)
    u_pass1=models.CharField(max_length=100)
    def __str__(self):

        return '{}'.format(self.u_name)
