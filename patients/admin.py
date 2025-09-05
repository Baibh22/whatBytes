from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date_of_birth', 'gender', 'phone_number', 'blood_group', 'created_by', 'created_at')
    list_filter = ('gender', 'blood_group', 'created_at', 'created_by')
    search_fields = ('first_name', 'last_name', 'phone_number', 'email')
    ordering = ('-created_at',)    
    fieldsets = (
        ('Basic Information', {
            'fields': ('first_name', 'last_name', 'date_of_birth', 'gender', 'phone_number', 'email', 'address')
        }),
        ('Medical Information', {
            'fields': ('blood_group', 'medical_history', 'allergies')
        }),
        ('Emergency Contact', {
            'fields': ('emergency_contact_name', 'emergency_contact_phone')
        }),
        ('System Information', {
            'fields': ('created_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('created_by')
