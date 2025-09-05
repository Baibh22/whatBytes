from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    """
    Serializer for Doctor model
    """
    full_name = serializers.ReadOnlyField()
    created_by_name = serializers.CharField(source='created_by.name', read_only=True)

    class Meta:
        model = Doctor
        fields = [
            'id', 'first_name', 'last_name', 'full_name', 'date_of_birth', 
            'gender', 'phone_number', 'email', 'address', 'specialization', 
            'license_number', 'years_of_experience', 'education', 
            'hospital_affiliation', 'consultation_fee', 'is_available', 
            'working_hours', 'created_by', 'created_by_name', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_at')

    def validate_date_of_birth(self, value):
        """
        Validate that the date of birth is not in the future
        """
        from django.utils import timezone
        if value > timezone.now().date():
            raise serializers.ValidationError("Date of birth cannot be in the future.")
        return value

    def validate_phone_number(self, value):
        """
        Basic phone number validation
        """
        if not value.isdigit() or len(value) < 10:
            raise serializers.ValidationError("Please enter a valid phone number.")
        return value

    def validate_years_of_experience(self, value):
        """
        Validate years of experience
        """
        if value < 0 or value > 50:
            raise serializers.ValidationError("Years of experience must be between 0 and 50.")
        return value

    def validate_consultation_fee(self, value):
        """
        Validate consultation fee
        """
        if value is not None and value < 0:
            raise serializers.ValidationError("Consultation fee cannot be negative.")
        return value


class DoctorCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating new doctors
    """
    class Meta:
        model = Doctor
        fields = [
            'first_name', 'last_name', 'date_of_birth', 'gender', 
            'phone_number', 'email', 'address', 'specialization', 
            'license_number', 'years_of_experience', 'education', 
            'hospital_affiliation', 'consultation_fee', 'is_available', 
            'working_hours'
        ]

    def validate_date_of_birth(self, value):
        """
        Validate that the date of birth is not in the future
        """
        from django.utils import timezone
        if value > timezone.now().date():
            raise serializers.ValidationError("Date of birth cannot be in the future.")
        return value

    def validate_phone_number(self, value):
        """
        Basic phone number validation
        """
        if not value.isdigit() or len(value) < 10:
            raise serializers.ValidationError("Please enter a valid phone number.")
        return value

    def validate_years_of_experience(self, value):
        """
        Validate years of experience
        """
        if value < 0 or value > 50:
            raise serializers.ValidationError("Years of experience must be between 0 and 50.")
        return value

    def validate_consultation_fee(self, value):
        """
        Validate consultation fee
        """
        if value is not None and value < 0:
            raise serializers.ValidationError("Consultation fee cannot be negative.")
        return value
