from django.contrib import admin

from attendence.models import *
# Register your models here.

admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(CourseEntry)