# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#Models
from .models import Profile
from django.contrib.auth.models import User

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'website', 'phone_number', 'created', 'picture')
    list_display_links = ('user', 'phone_number')
    list_editable = ('website','picture')
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'phone_number')
    list_filter = (
        'created', 
        'updated', 
        'user__is_active',
        'user__is_staff')
    fieldsets = (
        ('Profile', {
            'fields': ('user', 'picture'),
        }),
        ('Extra Info', {
            'fields': (('website', 'phone_number'), 'biography')
        }),
        ('Metadata', {
            'fields': ('created', 'updated')
        })
    )
    readonly_fields = ('created', 'updated')

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)