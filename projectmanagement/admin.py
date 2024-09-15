from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Project, ProjectMaterial

# Register your models here.
admin.site.unregister(Group)


# Mix pofile info into user info
class ProfileInline(admin.StackedInline):
    model = Profile

class ProjectInline(admin.StackedInline):
    model = Project
    extra = 0


# Extend User model
class UserAdmin(admin.ModelAdmin):
    model = User
    # fields = ['username', 'first_name', 'last_name', 'email', 'date_joined']
    exclude = ['groups', 'user_permissions']
    list_display = ['id', 'username', 'first_name', 'last_name', 'email', 'date_joined']
    inlines = [ProfileInline, ProjectInline]


class MaterialInline(admin.StackedInline):
    model = ProjectMaterial
    extra = 0

# Extend User model
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'id', 'visibility', 'time_created', 'stars']
    inlines = [MaterialInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectMaterial)


