from django.db import models


# Create your models here.
class Student(models.Model):
    student_id = models.PositiveIntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    field_of_study = models.CharField(max_length=40)
    gpa = models.FloatField()

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'
