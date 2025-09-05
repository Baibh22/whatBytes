from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialization', 'license_number', 'years_of_experience', 'is_available', 'created_by', 'created_at')
    list_filter = ('specialization', 'is_available', 'gender', 'created_at', 'created_by')
    search_fields = ('first_name', 'last_name', 'email', 'license_number', 'specialization')
    ordering = ('-created_at',)    
    fieldsets = (
        ('Basic Information', {
            'fields': ('first_name', 'last_name', 'date_of_birth', 'gender', 'phone_number', 'email', 'address')
        }),
        ('Professional Information', {
            'fields': ('specialization', 'license_number', 'years_of_experience', 'education', 'hospital_affiliation', 'consultation_fee')
        }),
        ('Availability', {
            'fields': ('is_available', 'working_hours')
        }),
        ('System Information', {
            'fields': ('created_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('created_by')
