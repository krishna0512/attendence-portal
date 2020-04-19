from datetime import datetime, timedelta
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.dates import MonthArchiveView, DayArchiveView
from django.views.decorators.csrf import csrf_exempt

from attendence.models import *

# Create your views here.

class IndexTemplateView(TemplateView):
    template_name = 'attendence/index.html'

class StudentListView(ListView):
    model = Student
    navigation = 'student'

class StudentDetailView(DetailView):
    model = Student
    slug_field = 'roll_number'

class SemesterListView(ListView):
    model = Semester
    navigation = 'semester'

class SemesterDetailView(DetailView):
    model = Semester

class CourseDetailView(DetailView):
    model = Course

class CourseListView(ListView):
    model = Course
    navigation = 'course'