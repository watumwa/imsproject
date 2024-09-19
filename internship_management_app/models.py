from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model


class User(AbstractUser):
    GENDER_OPTIONS=[
        ("M","MALE"),
        ("F","FEMALE")
    ]
    is_university_supervisor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_faculty_cordinator = models.BooleanField(default=False)
    registration_number= models.CharField(max_length=15)
    email =models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=15)
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=GENDER_OPTIONS)


class Internship_period(models.Model):
    STATUS_OPTIONS = [
        ("On Going","On Going"),
        ("Pending","Pending"),
        ("Ended","Ended"),
        
    ] 
    academic_year =models.CharField(max_length =9)
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    status = models.CharField(max_length=255,choices=STATUS_OPTIONS)






class Student_registration(models.Model):
    GENDER_OPTIONS=[
        ("M","MALE"),
        ("F","FEMALE")
    ]
    COURSE_OPTIONS=[
        ("BIT","Bacheclor of Information Technology"),
        ("LLB","Bachelor of Laws"),
        ("BBS","Bachelor of Business Studies"),
        ("BHRM","Bachelor of Human Resource"),
        ("BPA","Bachelor of Public Administration"),
        ("BSAS","Bachelor of Secretariate Studies"),
        ("DCIT","Deploma In Computer Science and Information Technology"),
        ("DBS","Deploma In Business Studies"),
        ("BCS","Bachelor of Computer Science"),
        ("BPL","Bachelor of Procuament and Logistics"),
        
    ]
    name =models.CharField(max_length=50)
    # gender = models.CharField(max_length=10, choices=GENDER_OPTIONS)
    phone_number = models.CharField(max_length=15)
    course = models.CharField(max_length=100,choices=COURSE_OPTIONS)
    email =models.EmailField(max_length=250)
    organization = models.CharField(max_length=100)
    placement_letter = models.FileField(blank=True, null=True, upload_to='placement_letters/')
   
    def __str__(self):
        return self.name

class InternshipReport(models.Model):
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    report = models.FileField(upload_to='reports/')
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.report.name





class Allocation(models.Model):
    intern = models.ForeignKey(Student_registration, on_delete=models.CASCADE)
    allocation_date = models.DateField(auto_now=False)
    supervisor = models.ForeignKey(User,on_delete=models.CASCADE)
    
        
class Placement(models.Model):
    organisation_name=models.CharField(max_length=255)
    address =models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    student_name = models.ForeignKey(Student_registration,on_delete=models.CASCADE)
    work_supervisor =models.CharField(max_length=20)
    contact =models.CharField(max_length=15)
    #location =models.PointField()



class Daily_activity(models.Model):
    department_of_attachment = models.CharField(max_length=50)
    date = models.DateField(auto_now=False)
    description_of_daily_activity = models.TextField(max_length=10000)
    lessons_and_skills_learnt = models.TextField(max_length=500)
    challenges = models.TextField(max_length=500)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='create_daily_activitiy')
    university_supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supervisor_daily_activities')


class Supervisor_visits(models.Model):
    visit_date = models.DateField(auto_now=False)
    intern = models.ForeignKey(Student_registration, on_delete=models.CASCADE)
    # supervisor = models.ForeignKey(User, on_delete=models.CASCADE)
    university_supervisor_comment = models.TextField(max_length=1000)
    work_supervisor_comment = models.TextField(max_length=1000)
    
     





class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Assigned_students(models.Model):
    student = models.ForeignKey(Student_registration, on_delete=models.CASCADE)
    university_supervisor = models.ForeignKey(User, related_name='assigned_students_university', on_delete=models.CASCADE)
   
@receiver(post_save, sender=Assigned_students)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            supervisor=instance.university_supervisor,
            message=f"A new student has been assigned to you: {instance.student.name}"
        )

    
class Comment(models.Model):
    student = models.ForeignKey(Student_registration, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.student.name} at {self.created_at}"




class Notification(models.Model):
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message









