from internship_management_app.models import Announcement

def announcements_context(request):
    announcements = Announcement.objects.all().order_by('-created_at')[:5]
    return {'announcements': announcements}
