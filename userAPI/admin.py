from django.contrib import admin
from django.contrib.auth.models import Group
from .models import UserProfile
from django.utils.safestring import mark_safe
from api_example import settings

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'image_', 'first_name', 'last_name', 'is_active')
    fieldsets = (
        ('Personal information:', {'fields': ('username', 'email', 'first_name', 'last_name', 'avatar')}),
        ('Permissions:', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('date_joined',)})
    )
    filter_horizontal = ('groups', 'user_permissions',)
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    # change_form_template = 'admin/userAPI/avatar_view.html'

    def image_(self, obj):
        if obj.avatar:
            return mark_safe('<img src="{}{}" width="auto" height="80" />'.format(
                settings.MEDIA_URL, obj.avatar))
        return "----"
admin.site.site_header = "Admin Page"
admin.site.unregister(Group)
admin.site.register(UserProfile, UserProfileAdmin)
