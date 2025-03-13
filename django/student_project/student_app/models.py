from django.db import models
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    accommodation_type = models.CharField(max_length=20)

class AcademicDetails(models.Model):
    #student = models.OneToOneField(Student, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    from_year = models.IntegerField()
    to_year = models.IntegerField()
    department_name = models.CharField(max_length=100)
    college_name = models.CharField(max_length=100)
    university_name = models.CharField(max_length=100)
    cgpa = models.FloatField()
