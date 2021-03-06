from datetime import datetime, timedelta
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
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

class StudentCreateView(CreateView):
    model = Student
    template_name_suffix = '_create_form'
    fields = '__all__'

class StudentDetailView(DetailView):
    model = Student
    slug_field = 'roll_number'

class SemesterListView(ListView):
    model = Semester
    navigation = 'semester'

class SemesterDetailView(DetailView):
    model = Semester

class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course

class CourseListView(ListView):
    model = Course
    navigation = 'course'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(faculty_primary__user=self.request.user)
        return queryset