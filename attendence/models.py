from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
import datetime

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile_student',
    )
    name = models.CharField(
        default='',
        max_length=100,
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

    def __str__(self):
        return self.name

class Faculty(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile_faculty',
    )
    name = models.CharField(
        default='',
        max_length=100,
    )
    faculty_id = models.CharField(
        blank=False,
        null=False,
        default='',
        max_length=30,
        unique=True,
        verbose_name='Faculty ID',
    )
    department = models.CharField(
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

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name

class Course(models.Model):
    DAY_CHOICE = (
        ('',''),
        ('0','Monday'),
        ('1','Tuesday'),
        ('2','Wednesday'),
        ('3','Thursday'),
        ('4','Friday'),
        ('5','Saturday'),
        ('6','Sunday'),
    )

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
        blank=True,
        related_name='courses_secondary',
    )
    day1 = models.CharField(
        choices=DAY_CHOICE,
        max_length=10,
        default='',
        blank=True,
        null=False,
    )
    day2 = models.CharField(
        choices=DAY_CHOICE,
        max_length=10,
        default='',
        blank=True,
        null=False,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('attendence:course-detail', kwargs={'pk': self.pk})

class CourseEntry(models.Model):
    """Each entry in calender class contains  the record for a
    course runned on a particular date
    """
    course = models.ForeignKey(
        'Course',
        null=False,
        on_delete=models.CASCADE,
        related_name='course_entries',
    )
    date = models.DateField(
        default=datetime.date.today,
    )
    # TODO: modify to include the various statues in choices
    status = models.CharField(
        default='active',
        max_length=30,
    )
