from typing import Type
from django.db import models
from django.db.models.options import Options
from .constants import GradeTypes


class Student(models.Model):
    name = models.CharField(max_length=100)
    marks = models.IntegerField()
    date_of_admission = models.DateField(auto_now_add=True)
    grade = models.CharField(choices=GradeTypes.choices, max_length=3)

    class Meta:
        db_table = 'student'
        verbose_name = 'student'
        verbose_name_plural = 'students'

    def __str__(self):
        return f'{self.name} || {self.pk}'
