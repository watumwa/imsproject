"""internship_management_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from internship_management_app.views import sign_up_view,index_view,internship_period_view,student_registration_view,home_view
from internship_management_app.views import allocate_intern_view,delete_daily_activity_view, allocate_intern_view,create_placement_view,daily_activity_view,supervisor_visit_view
from internship_management_app.views import edit_daily_activity_view,edit_internship_view,edit_placement_view, edit_student_view,delete_internship_period_view,delete_student_view,edit_allocation_view,delete_allocation_view
from django.conf import settings
from internship_management_app.views import view_reports, supervisor_visit_view,edit_supervisor_visit_view,delete_supervisor_visit_view
from django.conf.urls.static import static
from internship_management_app import views
from django.contrib.auth.views import LoginView
from internship_management_app.views import  assignment_success,assign_students,user_created,student_list,comment_view,worker_student_list,create_user
from internship_management_app.views import password_change,assigned_students_list,supervisor_visits_f_view
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',index_view,name='index_page'),
    path('home',home_view,name='home page'),
    #remeber to leave this blank the login url
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('user_created/',user_created, name='user_created'),
    path('sign_up/',sign_up_view,name = 'sign_up_page'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('create_user',create_user, name='create_user'),
    path('password_change/',password_change,name='password_change'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('add_announcement/', views.add_announcement, name='add_announcement'),
    path('notifications/', views.notification_list, name='notification_list'),
    







    path('view-reports/', view_reports, name='view_reports'),
    #  path('edit-report/<int:report_id>/', views.edit_report_view, name='edit_report'),
    # path('delete-report/<int:report_id>/', views.delete_report_view, name='delete_report'),


    path('assign_student',assign_students, name='assign_students'),
    path('assignment_success/', assignment_success, name='assignment_success'),
    path('assigned_students/',assigned_students_list, name='assigned_students_list'),

    path('apply/', views.apply_internship, name='apply_internship'),
    path('search/', views.search_internship, name='search_internship'),

    path('upload/', views.upload_report_view, name='upload_report'),
    path('delete/<int:report_id>/', views.delete_report_view, name='delete_report'),
    
    path('students/',student_list, name='student_list'),
    path('comment_page/<int:student_id>/',comment_view, name='comment_page'),
    path('students/',worker_student_list, name='worker_student_list'),
    path('daily-activity/', views.supervisor_daily_activity_view, name='daily_activity'),
    path('university-supervisor-daily-activity/', views.university_supervisor_daily_activity_view, name='university_supervisor_daily_activity'),
    
    path('view-placement-letters/', views.view_placement_letter, name='view_placement_letter'),
    
    # path('supervisor/<int:supervisor_id>/', views.supervisor_detail, name='supervisor_detail'),
    path('student-registration/',student_registration_view,name='student_registration'),
    path('edit_student/<int:student_id>/',edit_student_view,name='edit_student_page'),
    path('delete_student/<int:student_id>/',delete_student_view, name ='delete_student_page'),

    path('internship_period/create/',internship_period_view,name='create_internship_period'),
    path('edit_internship_period/<int:internship_id>/',edit_internship_view,name='edit_internship_period_page'),
    path('delete_internship_period/<int:internship_id>/',delete_internship_period_view, name ='delete_internship_period_page'),

   

    path('allocation/allocate/',allocate_intern_view, name='allocate_intern'),
    path('add_allocation/',allocate_intern_view,name='add_allocate_page'),
    path('edit_allocation/<int:allocation_id>/',edit_allocation_view,name='edit_allocation_page'),
    path('delete_allocation/<int:allocation_id>/',delete_allocation_view, name ='delete_allocation_page'),
    
  

    path('placement/create/', create_placement_view, name='create_placement'),
    path('edit_placement/<int:placement_id>/',edit_placement_view,name='edit_placement_page'),

    path('daily_activity/create/',daily_activity_view, name='create_daily_activity'),
    path('edit_daily_activity/<int:daily_activity_id>/',edit_daily_activity_view,name='edit_daily_activity_page'),
    path('delete_daily_activity/<int:daily_activity_id>/',delete_daily_activity_view, name ='delete_daily_activity_page'),
    path('supervisor-visits/', supervisor_visits_f_view, name='supervisor_visits'),
    path('supervisor_visit/create/',supervisor_visit_view, name='create_supervisor_visit'),
    path('edit_supervisor_visit/<int:supervisor_visit_id>/',edit_supervisor_visit_view, name='edit_supervisor_visit_page'),
    path('delete_supervisor_visit/<int:supervisor_visits_id>/',delete_supervisor_visit_view, name ='delete_supervisor_visit_page'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)