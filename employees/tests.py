from django.test import TestCase
from rest_framework.test import APIClient
from .models import Employee
from django.contrib.auth.models import User

class EmployeeAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        Employee.objects.create(name='Alice', email='alice@example.com', department='HR')
        Employee.objects.create(name='Bob', email='bob@example.com', department='Engineering')

    def test_list_employees(self):
        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, 200)

    def test_create_employee(self):
        data = {'name': 'Charlie', 'email': 'charlie@example.com', 'department': 'Sales'}
        response = self.client.post('/api/employees/', data)
        self.assertEqual(response.status_code, 201)

    def test_duplicate_email_error(self):
        data = {'name': 'Alice', 'email': 'alice@example.com', 'department': 'HR'}
        response = self.client.post('/api/employees/', data)
        self.assertEqual(response.status_code, 400)