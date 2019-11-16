from django.db import models

# Create your models here.
class User(models.Model):
    FirstName = models.CharField(max_length=264,unique=True)
    LastName = models.CharField(max_length=264,unique=True)
    Email = models.EmailField()


    def __str__(self):
        return self.FirstName,self.LastName,self.Email
