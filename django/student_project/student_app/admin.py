from django.contrib import admin
from .models import Student, AcademicDetails  # Import Models

# Register models to make them visible in Django Admin
admin.site.register(Student)
admin.site.register(AcademicDetails)