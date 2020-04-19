from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
import datetime

# Create your models here.

class Student(models.Model):
    # user = models.onetoonefield(
    #     user,
    #     on_delete=models.cascade,
    #     related_name='profile_student',
    # )
    name = models.CharField(
        default='',
        max_length=100,
    )
    email = models.CharField(
        default='',
        max_length=100,
    )
    roll_number = models.CharField(
        default='',
        max_length=30,
        unique=True,
    )
    year_of_enrollment = models.IntegerField(
        default=2020,
    )
    program = models.CharField(
        default='BTech',
        max_length=30,
    )
    status = models.CharField(
        blank=True,
        default='active',
        max_length=30,
    )
    gender = models.CharField(
        default='male',
        max_length=30,
    )

    def __str__(self):
        return self.name

class Faculty(models.Model):
    CATEGORY_CHOICES = (
        ('',''),
        ('fulltime','Full Time'),
        ('parttime','Part Time'),
        ('guest','Guest'),
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    name = models.CharField(
        default='',
        max_length=100,
    )
    faculty_id = models.CharField(
        default='',
        max_length=30,
        unique=True,
        verbose_name='Faculty ID',
    )
    category = models.CharField(
        choices=CATEGORY_CHOICES,
        max_length=50,
        default='',
    )
    department = models.CharField(
        default='',
        max_length=50,
        verbose_name='Department',
    )
    active = models.BooleanField(default=True)
    status = models.CharField(
        blank=True,
        default='active',
        max_length=30,
    )

    def __str__(self):
        return '{} ({})'.format(self.name, self.faculty_id)

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
    students_enrolled = models.ManyToManyField(
        'Student',
        blank=True,
        related_name='semsters',
    )

    def get_absolute_url(self):
        return reverse('attendence:semester-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

class CourseDetail(models.Model):
    """ This is equivalent for CourseMaster class.
    """
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
    TERM_CHOICES = (
        ('',''),
        ('spring','Spring'),
        ('monsoon','Monsoon'),
        ('summer','Summer'),
    )

    name = models.CharField(
        max_length=100,
        default='',
    )
    code = models.CharField(
        max_length=20,
        default='',
        unique=True,
    )
    credit = models.PositiveIntegerField(
        default=0,
    )
    term = models.CharField(
        choices=TERM_CHOICES,
        max_length=10,
        default='',
    )
    day1 = models.CharField(
        choices=DAY_CHOICE,
        max_length=10,
        default='',
        blank=True,
    )
    day2 = models.CharField(
        choices=DAY_CHOICE,
        max_length=10,
        default='',
        blank=True,
    )


class Course(models.Model):
    """ This is the equivalent class for CourseForSem.
    """
    course_detail = models.ForeignKey(
        'CourseDetail',
        null=True,
        on_delete=models.CASCADE,
        related_name='courses',
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
    approved = models.BooleanField(default=False)
    students_attended = models.ManyToManyField(
        'Student',
        blank=True,
        related_name='course_entries',
    )
