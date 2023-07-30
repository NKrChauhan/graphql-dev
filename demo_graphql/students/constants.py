from django.db import models


class GradeTypes(models.TextChoices):
    SPECIAL_GRADE = 'sp'
    FIRST = '1'
    SECOND = '2'
    THIRD = '3'
    F0RTH = '4'
