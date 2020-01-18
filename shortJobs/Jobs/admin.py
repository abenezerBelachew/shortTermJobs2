from django.contrib import admin
from .models import JobPost

# Register your models here.
@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',
        'photo', 'id', 'date_posted')