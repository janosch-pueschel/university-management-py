from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254, unique=True)
    academic_title = models.CharField(max_length=100, blank=True)


class CourseDescription(models.Model):
    description = models.TextField()
    course = models.OneToOneField("Course", on_delete=models.CASCADE)


class Semester(models.Model):
    title = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()


class Course(models.Model):
    title = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    students = models.ManyToManyField("Student")
    start_date = models.DateField()
    end_date = models.DateField()


class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254, unique=True)


class StudentId(models.Model):
    matriculation_number = models.Charfield(max_length=30, unique=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    issued_at = models.DateField()
    expires_at = models.DateField()
