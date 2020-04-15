from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile_student',
    )
    roll_number = models.CharField(
        blank=False,
        null=False,
        default='',
        max_length=30,
        unique=True,
    )
    year_of_enrollment = models.IntegerField(
        blank=False,
        null=False,
        default=2020,
    )
    program = models.CharField(
        blank=False,
        null=False,
        default='BTech',
        max_length=30,
    )
    status = models.CharField(
        blank=True,
        null=False,
        default='active',
        max_length=30,
    )
    gender = models.CharField(
        blank=False,
        null=False,
        default='male',
        max_length=30,
    )

class Faculty(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile_faculty',
    )
    fid = models.CharField(
        blank=False,
        null=False,
        default='',
        max_length=30,
        unique=True,
        verbose_name='Faculty ID',
    )
    dept = models.CharField(
        blank=False,
        null=False,
        default='',
        max_length=50,
        verbose_name='Department',
    )
    status = models.CharField(
        blank=True,
        null=False,
        default='active',
        max_length=30,
    )

class Semester(models.Model):
    name = models.CharField(
        max_length=30,
        default='',
    )
    academic_year = models.IntegerField(
        default=2020,
    )
    date_start = models.DateField(
        null=True,
    )
    date_end = models.DateField(
        null=True,
    )
    status = models.CharField(
        default='active',
        max_length=30,
    )
    def get_absolute_url(self):
        return reverse('attendence:semester-detail', kwargs={'pk': self.pk})

class Course(models.Model):
    name = models.CharField(
        max_length=100,
        default='',
    )
    credit = models.PositiveIntegerField(
        default=0,
    )
    semester = models.ForeignKey(
        'Semester',
        null=True,
        on_delete=models.CASCADE,
        related_name='courses',
    )
    date_start = models.DateField(
        null=True,
    )
    date_end = models.DateField(
        null=True,
    )
    faculty_primary = models.ForeignKey(
        'Faculty',
        null=True,
        on_delete=models.CASCADE,
        related_name='courses',
    )
    faculty_secondary = models.ManyToManyField(
        'Faculty',
        related_name='courses_secondary',
    )