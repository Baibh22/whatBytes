from django.contrib import admin
from .models import PatientDoctorMapping


@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'status', 'assigned_date', 'created_by', 'created_at')
    list_filter = ('status', 'assigned_date', 'created_at', 'created_by')
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__first_name', 'doctor__last_name')
    ordering = ('-created_at',)    
    fieldsets = (
        ('Mapping Information', {
            'fields': ('patient', 'doctor', 'status', 'notes')
        }),
        ('System Information', {
            'fields': ('assigned_date', 'created_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('assigned_date', 'created_at', 'updated_at')
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('patient', 'doctor', 'created_by')
