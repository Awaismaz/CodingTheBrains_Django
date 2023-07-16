from django.contrib import admin
from .models import Profile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display=('id','name','age','gender','occupation', 'email')
    list_display_links=('name','email')
    list_filter= ('gender','is_married')
    search_fields= ('occupation',)

admin.site.register(Profile, ProfileAdmin)

# admin.site.register(Profile)