from rest_framework import serializers
from .models import *


class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','name','email','department','role','date_joined']