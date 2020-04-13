from django.urls import path, include

from attendence import views

app_name = 'attendence'
urlpatterns = [
    path('index/', views.IndexTemplateView.as_view(), name='index'),
    path('semester/', views.SemesterListView.as_view(), name='semester-list'),
]