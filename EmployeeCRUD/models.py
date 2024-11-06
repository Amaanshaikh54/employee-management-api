from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100,null=False,error_messages={'invalid':'Enter name!!'})  
    email=models.EmailField(null=True,unique=True,error_messages={'invalid':'This email is already used Try another email'})
    department=models.CharField(max_length=100)
    role=models.CharField(max_length=100,null=True)
    date_joined=models.DateField(auto_now=True)
     
    class Meta:
        ordering = ['id'] 
