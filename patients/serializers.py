from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    """
    Serializer for Patient model
    """
    full_name = serializers.ReadOnlyField()
    created_by_name = serializers.CharField(source='created_by.name', read_only=True)

    class Meta:
        model = Patient
        fields = [
            'id', 'first_name', 'last_name', 'full_name', 'date_of_birth', 
            'gender', 'phone_number', 'email', 'address', 'blood_group', 
            'medical_history', 'allergies', 'emergency_contact_name', 
            'emergency_contact_phone', 'created_by', 'created_by_name', 
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


class PatientCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating new patients
    """
    class Meta:
        model = Patient
        fields = [
            'first_name', 'last_name', 'date_of_birth', 'gender', 
            'phone_number', 'email', 'address', 'blood_group', 
            'medical_history', 'allergies', 'emergency_contact_name', 
            'emergency_contact_phone'
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
