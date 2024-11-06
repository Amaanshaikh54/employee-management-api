from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100,null=False,error_messages={'invalid':'Enter name!!'})
    email = models.EmailField(null=True,unique=True,error_messages={'invalid':'This email is already used Try another email'})
    department = models.CharField(max_length=50, null=True, blank=True)
    role = models.CharField(max_length=50, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
