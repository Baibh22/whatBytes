from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Patient
from .serializers import PatientSerializer, PatientCreateSerializer


@api_view(['POST'])
def create_patient(request):
    """
    Create a new patient
    """
    serializer = PatientCreateSerializer(data=request.data)
    if serializer.is_valid():
        patient = serializer.save(created_by=request.user)
        response_serializer = PatientSerializer(patient)
        return Response({
            'message': 'Patient created successfully',
            'patient': response_serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_patients(request):
    """
    Retrieve all patients created by the authenticated user
    """
    patients = Patient.objects.filter(created_by=request.user)
    serializer = PatientSerializer(patients, many=True)
    return Response({
        'patients': serializer.data,
        'count': patients.count()
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_patient(request, patient_id):
    """
    Get details of a specific patient
    """
    patient = get_object_or_404(Patient, id=patient_id, created_by=request.user)
    serializer = PatientSerializer(patient)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_patient(request, patient_id):
    """
    Update patient details
    """
    patient = get_object_or_404(Patient, id=patient_id, created_by=request.user)
    serializer = PatientSerializer(patient, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'Patient updated successfully',
            'patient': serializer.data
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_patient(request, patient_id):
    """
    Delete a patient record
    """
    patient = get_object_or_404(Patient, id=patient_id, created_by=request.user)
    patient.delete()
    return Response({
        'message': 'Patient deleted successfully'
    }, status=status.HTTP_200_OK)