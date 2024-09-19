from django.contrib.auth.backends import ModelBackend

class RoleBasedBackend(ModelBackend):
    def get_user_role(self, user):
        # Define your logic to determine the user's role
        # For example, you can check the user's group or custom user attribute
        
        # Return the role ('student' or 'supervisor')
        return user.role  # Replace 'role' with the appropriate attribute or logic for getting the user's role

    def get_redirect_url(self, request, user):
        role = self.get_user_role(user)

        if role == 'student':
            return 'base_student.html'  # Replace with the URL path for the student base template
        elif role == 'supervisor':
            return 'base_supervisor.html'  # Replace with the URL path for the supervisor base template

        # If the role is not student or supervisor, you can handle it accordingly
        # For example, you can redirect to a generic base template or show an error page
        return '/base/general/'  # Replace with the URL path for a generic base template or error page
