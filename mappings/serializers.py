from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.models import Patient
from doctors.models import Doctor


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    """
    Serializer for PatientDoctorMapping model
    """
    patient_name = serializers.CharField(source='patient.full_name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.full_name', read_only=True)
    created_by_name = serializers.CharField(source='created_by.name', read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = [
            'id', 'patient', 'patient_name', 'doctor', 'doctor_name', 
            'status', 'assigned_date', 'notes', 'created_by', 'created_by_name', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ('id', 'assigned_date', 'created_by', 'created_at', 'updated_at')

    def validate(self, attrs):
        """
        Validate that the patient and doctor are not already mapped
        """
        patient = attrs.get('patient')
        doctor = attrs.get('doctor')
        
        if patient and doctor:
            existing_mapping = PatientDoctorMapping.objects.filter(
                patient=patient, 
                doctor=doctor
            ).exclude(id=self.instance.id if self.instance else None)
            
            if existing_mapping.exists():
                raise serializers.ValidationError(
                    "This patient is already assigned to this doctor."
                )
        
        return attrs


class PatientDoctorMappingCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating new patient-doctor mappings
    """
    class Meta:
        model = PatientDoctorMapping
        fields = ['patient', 'doctor', 'status', 'notes']

    def validate(self, attrs):
        """
        Validate that the patient and doctor are not already mapped
        """
        patient = attrs.get('patient')
        doctor = attrs.get('doctor')
        
        if patient and doctor:
            existing_mapping = PatientDoctorMapping.objects.filter(
                patient=patient, 
                doctor=doctor
            )
            
            if existing_mapping.exists():
                raise serializers.ValidationError(
                    "This patient is already assigned to this doctor."
                )
        
        return attrs


class PatientDoctorListSerializer(serializers.ModelSerializer):
    """
    Serializer for listing patient-doctor mappings with detailed information
    """
    patient_name = serializers.CharField(source='patient.full_name', read_only=True)
    patient_phone = serializers.CharField(source='patient.phone_number', read_only=True)
    doctor_name = serializers.CharField(source='doctor.full_name', read_only=True)
    doctor_specialization = serializers.CharField(source='doctor.specialization', read_only=True)
    doctor_phone = serializers.CharField(source='doctor.phone_number', read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = [
            'id', 'patient', 'patient_name', 'patient_phone', 
            'doctor', 'doctor_name', 'doctor_specialization', 'doctor_phone',
            'status', 'assigned_date', 'notes', 'created_at', 'updated_at'
        ]
