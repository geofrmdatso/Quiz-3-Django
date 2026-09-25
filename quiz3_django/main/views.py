from django.shortcuts import render
from .models import Student


def home(request):
    students = Student.objects.all().order_by('last_name')
    context = {
        'students': students,
        'total_students': students.count(),
    }
    return render(request, 'main/home.html', context)
