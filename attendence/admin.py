from django.contrib import admin
from django.urls import reverse_lazy

from attendence.models import *
# Register your models here.

admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Semester)
admin.site.register(CourseDetail)
admin.site.register(Course)
admin.site.register(Class)

admin.site.site_url = reverse_lazy('attendence:index')