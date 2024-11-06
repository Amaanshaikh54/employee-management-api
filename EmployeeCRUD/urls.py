from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('employees', Empview,basename='emp-api')

urlpatterns = [
    path('', include(router.urls)), 
    path('<int:pk>', include(router.urls)), 
    path('emplistview',EmployeeListView.as_view(),name='emplv')
]
