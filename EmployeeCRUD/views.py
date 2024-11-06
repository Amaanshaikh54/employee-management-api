from django.shortcuts import render
from .models import *
from rest_framework import viewsets,generics
from .serializers import EmpSerializer
from EmployeeCRUD.models import Employee

class Empview(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('id')
    serializer_class=EmpSerializer

class EmployeeListView(generics.ListAPIView):
    serializer_class = EmpSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()
        department = self.request.query_params.get('department')
        role = self.request.query_params.get('role')
        
        if department:
            queryset = queryset.filter(department=department)
        if role:
            queryset = queryset.filter(role=role)
        
        return queryset