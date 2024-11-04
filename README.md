Employee Management API
This is a RESTful API built with Django and Django REST Framework (DRF) for managing employees in a company. It supports CRUD operations, filtering, pagination, and token-based authentication.

Project Overview
The Employee Management API allows you to:

Create, retrieve, update, and delete employee records.
Filter employees by department and role.
Paginate results to show 10 employees per page.
Secure endpoints using token-based authentication.
Getting Started
Prerequisites
Python 3.x
Django and Django REST Framework
Installation
Clone the Repository:
git clone https://github.com/Amaanshaikh54/employee-management-api.git
cd employee-management-api
Create and Activate a Virtual Environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Dependencies:
pip install -r requirements.txt
Run Migrations:

python manage.py migrate
Create a Superuser (for accessing Django admin and generating tokens):

python manage.py createsuperuser
Start the Server:

python manage.py runserver
API Endpoints
Authentication
Obtain Token:
Endpoint: /api-token-auth/
Method: POST
Payload: { "username": "<your_username>", "password": "<your_password>" }
Description: Returns a token, which you must use in the Authorization header as Token <your_token> for authenticated requests.
Employee CRUD Operations
List All Employees (with Filtering and Pagination):

Endpoint: /api/employees/
Method: GET
Query Parameters:
department: Filter by department.
role: Filter by role.
page: Specify the page number.
Example: /api/employees/?department=HR&page=2
Create an Employee:

Endpoint: /api/employees/
Method: POST
Payload:
json
Copy code
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "department": "Engineering",
  "role": "Developer"
}
Retrieve a Single Employee:

Endpoint: /api/employees/{id}/
Method: GET
Update an Employee:

Endpoint: /api/employees/{id}/
Method: PUT
Payload:
json
Copy code
{
  "name": "John Smith",
  "department": "HR",
  "role": "Manager"
}
Delete an Employee:

Endpoint: /api/employees/{id}/
Method: DELETE
Error Handling
400 Bad Request: For validation errors (e.g., duplicate email).
404 Not Found: For invalid employee IDs.
201 Created: For successful creation of an employee.
204 No Content: For successful deletion.
Testing the API
You can use Postman to test the API. After obtaining a token, add it to your Authorization header for secure access:

Authorization Type: Token
Token: <your_token>
Project Structure
employees: Django app for employee management.
models.py: Defines the Employee model.
views.py: Contains the API views for CRUD operations.
serializers.py: Serializers for converting Employee instances to JSON.
urls.py: Defines URL patterns for the API.
