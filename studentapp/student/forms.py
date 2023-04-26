from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Course, Student, Result

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'family_name', 'date_of_birth', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('.com') or '@' not in email:
            raise forms.ValidationError('Invalid email address')
        return email

    def clean_date_of_birth(self):
        dob = self.cleaned_data.get('date_of_birth')
        today = timezone.now().date()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if age < 10:
            raise forms.ValidationError('Students must be at least 10 years old')
        return dob
    
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name']

    def clean_name(self):
        course_name = self.cleaned_data.get('course_name')
        if not course_name.isalpha():
            raise forms.ValidationError('Course name should only contain alphabets')
        return course_name
    
class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['course', 'student', 'score']

    def clean_score(self):
        score = self.cleaned_data.get('score')
        if score not in ['A', 'B', 'C', 'D', 'E', 'F']:
            raise forms.ValidationError('Invalid score')
        return score
    
    def clean(self):
        cleaned_data = super().clean()
        student = cleaned_data.get('student')
        course = cleaned_data.get('course')
        if Result.objects.filter(student=student, course=course).exists():
            raise ValidationError('Result already exists for this student and course')
        return cleaned_data
    