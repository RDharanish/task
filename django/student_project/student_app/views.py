from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, AcademicDetails

def student_details(request):
    if request.method == "POST":

        full_name = request.POST.get('full_name', '')
        print(full_name)

        student_id = request.POST.get('student_id', '')
        print(student_id)
        email = request.POST.get('email', '')
        print(email)
        phone_number = request.POST.get('phone_number', '')
        print(phone_number)
        address = request.POST.get('address', '')
        print(address)
        gender = request.POST.get('gender', '')
        print(gender)
        date_of_birth = request.POST.get('date_of_birth', '')
        print(date_of_birth)
        accommodation_type = request.POST.get('accommodation_type', '')
        print(accommodation_type)

        if not all([full_name, student_id, email, phone_number, address, gender, date_of_birth, accommodation_type]):
            return render(request, 'student-details.html', {'error': "All fields are required!"})

        student = Student.objects.create(
            full_name=full_name,
            student_id=student_id,
            email=email,
            phone_number=phone_number,
            address=address,
            gender=gender,
            date_of_birth=date_of_birth,
            accommodation_type=accommodation_type
        )
        print(student)

        #return redirect('academic-details.html')

    return render(request, 'student-details.html')


def academic_details(request):
   # student = get_object_or_404(Student, id=student_id)
    
    if request.method == "POST":
        course_name = request.POST.get('course_name', '')
        print(college_name)
        from_year = request.POST.get('from_year', '')
        print(from_year)
        to_year = request.POST.get('to_year', '')
        print(to_year)
        department_name = request.POST.get('department_name', '')
        print(department_name)
        college_name = request.POST.get('college_name', '')
        print(college_name)
        university_name = request.POST.get('university_name', '')
        print(university_name)
        cgpa = request.POST.get('cgpa', '')
        print(cgpa)

        if not all([course_name, from_year, to_year, department_name, college_name, university_name, cgpa]):
            return render(request, 'academic-details.html', {'error': "All fields are required!"})# 'student': student})

        academy= AcademicDetails.objects.create(
            #student=student,
            course_name=course_name,
            from_year=from_year,
            to_year=to_year,
            department_name=department_name,
            college_name=college_name,
            university_name=university_name,
            cgpa=cgpa
        )
        print(academy)

        return redirect('academic-details.html')  # Change this to your success page

    return render(request, 'academic-details.html')#{'student': student})
