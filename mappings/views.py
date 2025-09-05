from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import PatientDoctorMapping
from .serializers import (
    PatientDoctorMappingSerializer, 
    PatientDoctorMappingCreateSerializer,
    PatientDoctorListSerializer
)


@api_view(['POST'])
def create_mapping(request):
    """
    Assign a doctor to a patient
    """
    serializer = PatientDoctorMappingCreateSerializer(data=request.data)
    if serializer.is_valid():
        mapping = serializer.save(created_by=request.user)
        response_serializer = PatientDoctorMappingSerializer(mapping)
        return Response({
            'message': 'Doctor assigned to patient successfully',
            'mapping': response_serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_mappings(request):
    """
    Retrieve all patient-doctor mappings
    """
    mappings = PatientDoctorMapping.objects.all()
    serializer = PatientDoctorListSerializer(mappings, many=True)
    return Response({
        'mappings': serializer.data,
        'count': mappings.count()
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_patient_doctors(request, patient_id):
    """
    Get all doctors assigned to a specific patient
    """
    mappings = PatientDoctorMapping.objects.filter(patient_id=patient_id)
    serializer = PatientDoctorListSerializer(mappings, many=True)
    return Response({
        'patient_doctors': serializer.data,
        'count': mappings.count()
    }, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_mapping(request, mapping_id):
    """
    Remove a doctor from a patient
    """
    mapping = get_object_or_404(PatientDoctorMapping, id=mapping_id, created_by=request.user)
    mapping.delete()
    return Response({
        'message': 'Doctor-patient mapping removed successfully'
    }, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_mapping(request, mapping_id):
    """
    Update patient-doctor mapping status or notes
    """
    mapping = get_object_or_404(PatientDoctorMapping, id=mapping_id, created_by=request.user)
    serializer = PatientDoctorMappingSerializer(mapping, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'Mapping updated successfully',
            'mapping': serializer.data
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)