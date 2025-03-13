from django.urls import path
from .views import student_details, academic_details

urlpatterns = [
    path('', student_details, name='student_details'),
    path('academic-details', academic_details, name='academic_details'),
]
