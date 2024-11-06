from django.contrib import admin
from .models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','name','email','department','role','date_joined']

admin.site.register(Employee,EmployeeAdmin)