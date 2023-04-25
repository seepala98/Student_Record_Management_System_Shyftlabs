from django.urls import path
from .views import StudentsListView, AddStudentView, DeleteStudentView, AddCourseView, CoursesListView, DeleteCourseView, AddResultView, ResultsListView 
from . import views

app_name = 'student'


urlpatterns = [
    path('', views.home, name='home'),
    path('student_list/', StudentsListView.as_view(), name='student_list'),
    path('add_student/', AddStudentView.as_view(), name='add_student'),
    path('delete_student/<int:pk>/', DeleteStudentView.as_view(), name='delete_student'),
    path('add_course/', AddCourseView.as_view(), name='add_course'),
    path('course_list/', CoursesListView.as_view(), name='course_list'),
    path('delete_course/', DeleteCourseView.as_view(), name='delete_course'),
    path('add_result/', AddResultView.as_view(), name='add_result'),
    path('result_list/', ResultsListView.as_view(), name='result_list'),
]
