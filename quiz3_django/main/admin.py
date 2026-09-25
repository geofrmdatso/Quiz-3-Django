from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'course', 'year_level', 'email')
    search_fields = ('first_name', 'last_name', 'course')
    list_filter = ('course', 'year_level')
