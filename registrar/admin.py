from django.contrib import admin
from . import models
from .models import Student, Mentor


class AttachmentInline(admin.StackedInline):
    model = models.Attachment
    extra = 1
@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    # make list display all fields
    
    list_display = tuple([field.name for field in Student._meta.fields])
    # list_editable = (,)
    # list_per_page = 10
    # list_select_related = ['user']
    inlines = [AttachmentInline]
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
    
    
@admin.register(models.Mentor)
class MentorAdmin(admin.ModelAdmin):
    # make list display all fields
    
    list_display = tuple([field.name for field in Mentor._meta.fields])
    # list_editable = (,)
    # list_per_page = 10
    # list_select_related = ['user']
  
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']