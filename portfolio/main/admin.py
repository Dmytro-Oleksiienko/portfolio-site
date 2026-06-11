from django.contrib import admin
from .models import Profile, Skill, Project, Experience, ContactMessage

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Experience)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')
    
    def has_add_permission(self, request):
        return False  # Prevent adding messages manually from admin
