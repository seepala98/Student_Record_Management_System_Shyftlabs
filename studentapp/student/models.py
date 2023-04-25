from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    family_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.full_name} - ({self.email})'

    @property
    def full_name(self):
        return f'{self.first_name} {self.family_name}'


class Course(models.Model):
    course_name = models.CharField(max_length=200, unique=True, default='')

    def __str__(self):
        return self.course_name

class Result(models.Model):
    GRADE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.CharField(max_length=1, choices=GRADE_CHOICES)

    def __str__(self):
        return f"{self.student} - {self.course} - {self.score}"