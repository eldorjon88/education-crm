from django.contrib import admin

from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'status', 'is_risk', 'created_at')
    list_filter = ('status', 'is_risk')
    search_fields = ('full_name', 'phone')
