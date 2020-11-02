from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    salary=models.IntegerField()
    status=models.BooleanField()

'''class user_table(models.Model):
    username=models.CharField(max_length=20)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)'''