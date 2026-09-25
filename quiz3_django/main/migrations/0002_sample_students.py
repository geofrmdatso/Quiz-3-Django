from django.db import migrations


def add_sample_students(apps, schema_editor):
    Student = apps.get_model('main', 'Student')
    Student.objects.create(
        first_name='Juan',
        last_name='Dela Cruz',
        course='BS Computer Science',
        year_level=3,
        email='juan.delacruz@example.com',
    )
    Student.objects.create(
        first_name='Maria',
        last_name='Santos',
        course='BS Information Technology',
        year_level=2,
        email='maria.santos@example.com',
    )
    Student.objects.create(
        first_name='Pedro',
        last_name='Reyes',
        course='BS Computer Engineering',
        year_level=4,
        email='pedro.reyes@example.com',
    )


def remove_sample_students(apps, schema_editor):
    Student = apps.get_model('main', 'Student')
    Student.objects.filter(email__in=[
        'juan.delacruz@example.com',
        'maria.santos@example.com',
        'pedro.reyes@example.com',
    ]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_sample_students, remove_sample_students),
    ]
