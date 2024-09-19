from  django.forms import ModelForm,DateInput
from internship_management_app.models import Student_registration,Allocation,Supervisor_visits,Internship_period
from django import forms
from .models import Comment
from django import forms
from .models import InternshipReport

from django.contrib.auth.forms import UserCreationForm

from .models import User,Assigned_students
from .models import Internship_period,Daily_activity,Supervisor_visits
from internship_management_app.models import Placement,Announcement

from .models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2','registration_number','gender')


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content']





class ReportForm(forms.ModelForm):
    class Meta:
        model = InternshipReport
        fields = ['report']






class InternshipPeriodForm(forms.ModelForm):
    ACADEMIC_YEAR_CHOICES = [
        ('2020-2021', '2020-2021'),
        ('2021-2022', '2021-2022'),
        ('2022-2023', '2022-2023'),
        ('2024-2025', '2024-2025'),
    ]

    academic_year = forms.ChoiceField(choices=ACADEMIC_YEAR_CHOICES)
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Internship_period
        fields = ['academic_year', 'start_date', 'end_date', 'status']
        widgets = {
            'academic_year':DateInput(attrs={"type":"date"})
        }









class Student_registrationForm(ModelForm):
    class Meta:
        model = Student_registration
        fields=  [ 'name','phone_number','course', 'email','organization','placement_letter']

class Student_registrationForm(ModelForm):
    class Meta:
        model = Student_registration
        fields= '__all__'



# class SupervisorRegistrationForm(ModelForm):
#     class Meta:
#         model = Supervisor_registration
#         fields = '__all__'

# class WorksupervisorRegistrationForm(ModelForm):
#     class Meta:
#         model = Work_supervisor_registration
#         fields = '__all__'








class AllocationForm(ModelForm):
    class Meta:
        model = Allocation
        fields = ['intern', 'allocation_date', 'supervisor']
        widgets = {
            'allocation_date':DateInput(attrs={"type":"date"})
        }

class PlacementForm(forms.ModelForm):
    class Meta:
        model = Placement
        fields = ['organisation_name', 'address', 'department', 'student_name', 'work_supervisor', 'contact']






class DailyActivityForm(forms.ModelForm):
    class Meta:
        model = Daily_activity
        fields = ['department_of_attachment', 'date', 'description_of_daily_activity', 'lessons_and_skills_learnt', 'challenges','student']
        widgets = {
            'date':DateInput(attrs={"type":"date"})
        }




class SupervisorVisitsForm(forms.ModelForm):
    class Meta:
        model = Supervisor_visits
        fields = ['visit_date', 'intern','university_supervisor_comment', 'work_supervisor_comment']
        widgets = {
            'visit_date':DateInput(attrs={"type":"date"})
        }






class Supervisor_visitForm(ModelForm):
    class Meta:
        model = Supervisor_visits
        fields= '__all__'
        widgets = {
            "visit_date":DateInput(attrs={"type":"date"})
        }




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']



# class LoginForm(forms.Form):
#     username = forms.CharField(label='User Name', max_length=100)
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)

#     def clean(self):
#         cleaned_data = super().clean()
#         username = cleaned_data.get('username')
#         password = cleaned_data.get('password')

#         # Add your custom validation logic here
#         if not username or not password:
#             raise forms.ValidationError('Please enter both username and password.')
#         # You can add more validation rules if needed

#         return cleaned_data
    
