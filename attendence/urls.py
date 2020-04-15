from django.urls import path, include

from attendence import views

app_name = 'attendence'
urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),

    path('semester/', views.SemesterListView.as_view(), name='semester-list'),
    path('semester/<int:pk>/view/', views.SemesterDetailView.as_view(), name='semester-detail'),

    path('course/', views.CourseListView.as_view(), name='course-list'),
    path('course/<int:pk>/view/', views.CourseDetailView.as_view(), name='course-detail'),
]