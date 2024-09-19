from django.contrib import admin


from django.contrib.admin.models import LogEntry
from django.contrib.auth import get_user_model
from .models import Student_registration,Supervisor_visits,Allocation,Placement,Daily_activity,Internship_period
from .models import Announcement,User,Assigned_students
admin.site.register(Assigned_students)
admin.site.register(Announcement)
admin.site.register(LogEntry)
admin.site.register(Internship_period)
admin.site.register(Supervisor_visits)
admin.site.register(Daily_activity)
admin.site.register(Placement)
admin.site.register(Allocation)

admin.site.register(User)
