from django.shortcuts import render,redirect, get_object_or_404
from .forms import  Student_registrationForm,AllocationForm,ReportForm,CustomUserCreationForm, AnnouncementForm, PlacementForm,DailyActivityForm,SupervisorVisitsForm,InternshipPeriodForm,CommentForm
from .models import   Assigned_students,Announcement,Notification,InternshipReport, Daily_activity, Student_registration,Internship_period,Allocation,Supervisor_visits,Placement,Assigned_students
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required





@login_required
def index_view(request):
    
    return render(request, 'index.html')
@login_required
def home_view(request):
    
    return render(request, 'home.html')

def annoucement_view(request):
    announcement = Announcement.objects.all().order_by('-created_at')[:5]
    context = {'announcements': announcement}
    return render(request, 'registration/login.html',context)





@login_required
def supervisor_daily_activity_view(request):
    university_supervisor = request.user
    daily_activities = Daily_activity.objects.all()
    
    
    context = {
        'daily_activities': daily_activities
    }
    return render(request, 'daily_activity_supervisor.html', context)



@login_required
def view_placement_letter(request):
    students_with_placement_letters = Student_registration.objects.exclude(placement_letter__exact='')

    context = {
        'students_with_placement_letters': students_with_placement_letters,
    }

    return render(request, 'view_placement_letter.html', context)



def notification_list(request):
    supervisor = request.user
    notifications = Notification.objects.filter(supervisor=supervisor).order_by('-created_at')
    return render(request, 'notification_list.html', {'notifications': notifications})


User = get_user_model()

def assign_students(request):
    if request.method == 'POST':
        student_id = request.POST['student']
        supervisor_id = request.POST['supervisor']
        
        student = Student_registration.objects.get(id=student_id)
        supervisor = User.objects.get(id=supervisor_id)
        
        assigned_student = Assigned_students(student=student, university_supervisor=supervisor)
        assigned_student.save()
        
        return redirect('assignment_success') 
    
    students = Student_registration.objects.all()
    supervisors = User.objects.filter(is_university_supervisor=True)
    
    context = {
        'students': students,
        'supervisors': supervisors
    }
    
    return render(request, 'assign_students.html', context)

def assignment_success(request):
    return render(request, 'assignment_success.html')








User = get_user_model()

def create_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        
        if User.objects.filter(username=username).exists():
            return render(request, 'create_user.html', {'error_message': 'Username already exists.'})
        
        user = User.objects.create_user(username=username, password=password)
        
        if role == 'student':
            user.is_student = True
        elif role == 'university_supervisor':
            user.is_university_supervisor = True
        elif role == 'faculty_cordinator':
            user.is_faculty_cordinator = True
        
        user.save()
        
        return redirect('user_created')
    users = User.objects.all()
    context ={
            'users':users
        }
    
    return render(request, 'create_user.html',context)

def user_created(request):

    return render(request, 'user_created.html')











@login_required
def student_registration_view(request):
    if request.method == 'POST':
        studentregistration_form = Student_registrationForm(request.POST, request.FILES)
        if studentregistration_form.is_valid():
            student = studentregistration_form.save(commit=False)
            organization = student.organization
            student.save()
            
            if 'placement_letter' in request.FILES:
                placement_letter_file = request.FILES['placement_letter']
                fs = FileSystemStorage(location=settings.MEDIA_ROOT)
                filename = fs.save(placement_letter_file.name, placement_letter_file)
                student.placement_letter = filename
                student.save()

            messages.success(request, "Registered successfully") 
            return redirect('student_registration')  # Replace with the appropriate URL or view name
    else:
        studentregistration_form = Student_registrationForm()   
    
    students = Student_registration.objects.all() 
    context = {'form': studentregistration_form, 'students': students}
    return render(request, 'student_registration.html', context)


def edit_student_view(request,student_id):
    
  student =  Student_registration.objects.get(id=student_id)
  message =''

  if request.method == "POST":

    student_form =Student_registrationForm(request.POST,instance =student)
     
    if student_form.is_valid():
        student_form.save()
        message = "Changes made successfully"

    else:
        message = "Form is invalid"
        
  else:
    student_form = Student_registrationForm(instance =student)

  context = {
    'form':student_form,
    'student':student,
    'message':message
}
  return render(request,'edit_student.html',context)

def delete_student_view(request,student_id):
    student = Student_registration.objects.get(id = student_id)

    student.delete()
  
    return redirect (student_registration_view)




@login_required
def internship_period_view(request):
    if request.method == 'POST':
        internship_period_form = InternshipPeriodForm(request.POST)
        if internship_period_form.is_valid():
            internship_period_form.save()     
            
           
   
    internship_period_form = InternshipPeriodForm()
    
    internship = Internship_period.objects.all()
    context = {'form':internship_period_form, 'internship':internship}
    return render(request, 'internship_period.html',context)

def edit_internship_view(request,internship_id):
    internship =    Internship_period.objects.get(id=internship_id)
    if request.method =="POST":
       internship_period_form = InternshipPeriodForm(request.POST,instance =internship)

       if internship_period_form.is_valid():  
           internship_period_form.save() 

        
    internship_period_form =   InternshipPeriodForm(instance=internship)

    context ={
        'form':internship_period_form,
        'internship':internship
    }
        
    return render(request,'edit_internship_period.html',context)

def delete_internship_period_view(request,internship_id):
    internship_period = Internship_period.objects.get(id =internship_id)

    internship_period.delete()
  
    return redirect (internship_period_view)


 

@login_required
def allocate_intern_view(request):
    if request.method =='POST':
        allocation_form =AllocationForm(request.POST)
        if allocation_form.is_valid():
           allocation_form.save()
    else:
        allocation_form = AllocationForm()

    allocation = Allocation.objects.all

    context ={
        'form':allocation_form,
        'allocation':allocation,
    }
    return render(request,"allocate_intern.html",context)


def edit_allocation_view(request,allocation_id):
    allocation = Allocation.objects.get(id = allocation_id)
    if request.method =="POST":
       allocation_form = AllocationForm(request.POST,instance = allocation)

       if  allocation_form.is_valid():
            allocation_form.save()

        
    allocation_form =   AllocationForm(instance=allocation)

    context ={
        'form':allocation_form,
        'allocation':allocation
    }
        
    return render(request,'edit_allocation.html',context)

def delete_allocation_view(request,allocation_id):
    allocation = Allocation.objects.get(id = allocation_id)

    allocation.delete()
  
    return redirect (allocate_intern_view)





@login_required
def create_placement_view(request):
    if request.method == 'POST':
        placement_form = PlacementForm(request.POST)
        if  placement_form.is_valid():
            placement_form.save()
            
    else:
        placement_form = PlacementForm()

    placement =Placement.objects.all()

    context ={
        'form':placement_form,
        'placement':placement,
    }
    return render(request,"create_placement.html",context)

def edit_placement_view(request,placement_id):
    placement = Placement.objects.get(id = placement_id)
    if request.method =="POST":
       placement_form = PlacementForm(request.POST,instance = placement)

       if  placement_form.is_valid():
            placement_form.save()

        
    placement_form =   PlacementForm(instance=placement)

    context ={
        'form':placement_form,
        'placement':placement
    }
        
    return render(request,'edit_placement.html',context)
@login_required
def create_placement_view(request):
    if request.method == 'POST':
        placement_form = PlacementForm(request.POST)
        if  placement_form.is_valid():
            placement_form.save()
            
    else:
        placement_form = PlacementForm()

    placement =Placement.objects.all()

    context ={
        'form':placement_form,
        'placement':placement,
    }
    return render(request,"create_placement.html",context)





@login_required
def daily_activity_view(request):
    if request.method == 'POST':
        form = DailyActivityForm(request.POST)
        if form.is_valid():
            daily_activity = form.save(commit=False)
            daily_activity.university_supervisor = request.user
            daily_activity.save()
            
    else:
        form = DailyActivityForm()
    daily_activity = Daily_activity.objects.all()
    context = {
        'daily_activity':daily_activity,
        'form': form,
    }
    return render(request, 'create_daily_activity.html', context)


def edit_daily_activity_view(request,daily_activity_id):
    daily_activity = Daily_activity.objects.get(id = daily_activity_id)
    if request.method =="POST":
       daily_activity_form = DailyActivityForm(request.POST,instance = daily_activity)

       if  daily_activity_form.is_valid():
           daily_activity_form.save()

    
    daily_activity_form =   DailyActivityForm(instance=daily_activity)
    
    context ={
        'form':daily_activity_form,
        'daily_activity':daily_activity
    }
        
    return render(request,'edit_daily_activity.html',context)



def delete_daily_activity_view(request,daily_activity_id):
    daily_activity = Daily_activity.objects.get(id = daily_activity_id)

    daily_activity.delete()
  
    return redirect (daily_activity_view)






@login_required
def supervisor_visit_view(request):
    message =""
    if request.method == 'POST':
        supervisor_form = SupervisorVisitsForm(request.POST)
        if supervisor_form.is_valid():
            supervisor_form.save()
            message = "visit captured successfully"
            
    
    supervisor_form = SupervisorVisitsForm()
    messages.success(request,message)

    supervisor_visit = Supervisor_visits.objects.all()

    context ={'form':supervisor_form, 'supervisor_visit':supervisor_visit,'message':message}
    
    return render(request, 'create_supervisor_visit.html', context)

# views.py
def edit_supervisor_visit_view(request, supervisor_visit_id):
    supervisor_visit = Supervisor_visits.objects.get(id=supervisor_visit_id)
    message = ''

    if request.method == "POST":
        supervisor_visit_form = SupervisorVisitsForm(request.POST, instance=supervisor_visit)
     
        if supervisor_visit_form.is_valid():
            supervisor_visit_form.save()
            message = "Changes made successfully"
        else:
            message = "Form is invalid"
    else:
        supervisor_visit_form = SupervisorVisitsForm(instance=supervisor_visit)

    context = {
        'form': supervisor_visit_form,
        'supervisor_visit':supervisor_visit,
        'message': message
    }

    return render(request, 'edit_supervisor_visits.html', context)

 
def delete_supervisor_visit_view(request,supervisor_visits_id):
    supervisor_visit= Supervisor_visits.objects.get(id = supervisor_visits_id)

    supervisor_visit.delete()
  
    return redirect (supervisor_visit_view)





def sign_up_view(request):
    message = ""
    if request.method == "POST":
        sign_up_form = CustomUserCreationForm(request.POST)

        if sign_up_form.is_valid():
           sign_up_form.save()
           message = 'User created successfully'
        else:
            message = 'Something went wrong'

    else:
        sign_up_form = CustomUserCreationForm()

    context = {
        'form': sign_up_form,
        'message': message
    }

    return render(request, 'registration/sign_up.html', context)

def password_reset(request):
    return render(request, 'password_reset.html')

def password_reset_done(request):
    return render(request, 'password_reset_done.html')

def password_reset_confirm(request, uidb64, token):
    return render(request, 'password_reset_confirm.html', {'uidb64': uidb64, 'token': token})

def password_reset_complete(request):
    return render(request, 'password_reset_complete.html')











def password_change(request):
    if request.method == 'POST':
        form = auth_views.PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # return redirect('password_change_done')
    else:
        form = auth_views.PasswordChangeForm(request.user)
    
    context = {
        'form': form
    }
    
    return render(request, 'password_change.html', context)

def forgot_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                from_email='noreply@example.com',
                email_template_name='password_reset_email.html',
            )
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'forgot_password.html',context)








def apply_internship(request):
    if request.method == 'POST':
        # Handle form submission here
        pass
    return render(request, 'apply.html')

def search_internship(request):
    return render(request, 'search.html')



def upload_report_view(request):
    if request.method == 'POST':
        report_form = ReportForm(request.POST, request.FILES)
        if report_form.is_valid():
            report = report_form.save(commit=False)
            report.student = request.user
            report.save()
            # return redirect('view_reports')
    else:
        report_form = ReportForm()
    internship_report =InternshipReport.objects.all()
    
    context = {'form': report_form,'internship_report':internship_report}
    return render(request, 'upload_report.html', context)

def delete_report_view(request, report_id):
    report = get_object_or_404(InternshipReport,id=report_id)

    # Make sure the report belongs to the current user before deleting
    if report.student == request.user:
        report.delete()

    return redirect('view_reports')



def student_list(request):
    assigned_students = Assigned_students.objects.all()
   
    context = {
        'assigned_students':assigned_students,
    }
    return render(request, 'student_list.html', context)

def worker_student_list(request):
  
    worker_assigned_students = Assigned_students.objects.filter(work_supervisor=request.user)
    context = {
        'worker_assigned_students':worker_assigned_students,
    }
    return render(request, 'worker_student_list.html', context)



def comment_view(request, student_id):
    if request.method == 'POST':
        # Assuming you have a Comment model to store the comments
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.student_id = student_id
            comment.save()
            # Redirect to a success page or student detail page
            return redirect('comment.html', student_id=student_id)
    else:
        form = CommentForm()

    return render(request, 'comment.html', {'form': form})


def add_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('announcement_list')
    else:
        form = AnnouncementForm()
    
    context = {'form': form}
    return render(request, 'add_announcement.html', context)



def assigned_students_list(request):
    assigned_students = Assigned_students.objects.all()
    context = {
        'assigned_students': assigned_students
    }
    return render(request, 'assigned_student_list.html', context)


def supervisor_visits_f_view(request):
    supervisor_visits = Supervisor_visits.objects.all()
    context = {'supervisor_visits': supervisor_visits}
    return render(request, 'supervisor_visits_f.html',context)
def view_reports(request):
    reports = InternshipReport.objects.all()
    context = {'reports': reports}
    return render(request, 'view_reports.html', context)




def university_supervisor_daily_activity_view(request):
    university_supervisor = request.user
    daily_activities = Daily_activity.objects.filter(student__university_supervisor=university_supervisor)
    context = {
        'daily_activities': daily_activities
    }
    return render(request, 'university_supervisor_daily_activity.html', context)

