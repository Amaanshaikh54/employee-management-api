# Generated by Django 5.1.2 on 2024-11-04 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeCRUD', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_joined',
            field=models.DateField(auto_now=True),
        ),
    ]