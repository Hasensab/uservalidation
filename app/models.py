from django.db import models

# Create your models here.
class School(models.Model):
    sname=models.CharField(max_length=100)
    sprinciple=models.CharField(max_length=100)
    slocation=models.CharField(max_length=100)
    email=models.EmailField()
    reenteremail=models.EmailField()
    password=models.CharField(max_length=100,null=True)
    repass=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.sname