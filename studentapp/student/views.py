from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.urls import reverse_lazy
from .forms import StudentForm, CourseForm, ResultForm
from .models import Student, Course, Result
from django.views import View

# Create your views here.
def home(request):
    return render(request, 'student/home.html')

class AddStudentView(View):
    template_name = 'student/add_student.html'
    def get(self, request):
        form = StudentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            messages.success(request, 'Student added successfully')
            return redirect('student:add_student')
        else:
            messages.error(request, 'Please correct the errors below')
        return render(request, self.template_name, {'form': form})


class StudentsListView(ListView):
    model = Student
    template_name = 'student/student_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        students = Student.objects.all()
        context['students'] = students
        context['delete_url'] = reverse_lazy('delete_student')
        return context

class DeleteStudentView(View):
    def post(self, request, pk):
        student = Student.objects.get(pk=pk)
        student.delete()
        return redirect('student:student_list')

class CoursesListView(ListView):
    model = Course
    template_name = 'student/course_list.html'
    context_object_name = 'courses'
    ordering = ['course_name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'All Courses'
        return context

    def post(self, request, *args, **kwargs):
        course_id = request.POST.get('course_id')
        if course_id:
            try:
                course = Course.objects.get(id=course_id)
                course.delete()
                messages.success(request, f"Course '{course.course_name}' deleted successfully.")
            except Course.DoesNotExist:
                messages.error(request, "Course does not exist.")
        return redirect(reverse_lazy('course_list'))
    
class AddCourseView(View):
    template_name = 'student/add_course.html'

    def get(self, request):
        form = CourseForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            course.save()
            messages.success(request, f'Course "{course.course_name}" added successfully.')
            # form = CourseForm()
            return redirect('student:add_course')
        else:
            messages.error(request, 'Please correct the errors below.')
        return render(request, self.template_name, {'form': form})

class DeleteCourseView(View):
    def post(self, request):
        course_id = request.POST.get('course_id')
        if course_id:
            Course.objects.filter(id=course_id).delete()
            messages.success(request, 'Course deleted successfully')
        else:
            messages.error(request, 'Unable to delete course')
        return redirect('student:course_list')

class AddResultView(View):
    template_name = 'student/add_result.html'

    def get(self, request):
        form = ResultForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ResultForm(request.POST)
        if form.is_valid():
            result_form = form.save()
            result_form.save()
            messages.success(request, 'Result added successfully')
            return redirect('student:add_result')
        else:
            messages.error(request, 'Please correct the errors below')
        return render(request, self.template_name, {'form': form})

class ResultsListView(ListView):
    model = Result
    template_name = 'student/result_list.html'
    context_object_name = 'results'
    ordering = ['student']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'All Results'
        return context
