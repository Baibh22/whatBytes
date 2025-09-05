from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Doctor
from .serializers import DoctorSerializer, DoctorCreateSerializer


@api_view(['POST'])
def create_doctor(request):
    """
    Create a new doctor
    """
    serializer = DoctorCreateSerializer(data=request.data)
    if serializer.is_valid():
        doctor = serializer.save(created_by=request.user)
        response_serializer = DoctorSerializer(doctor)
        return Response({
            'message': 'Doctor created successfully',
            'doctor': response_serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_doctors(request):
    """
    Retrieve all doctors
    """
    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(doctors, many=True)
    return Response({
        'doctors': serializer.data,
        'count': doctors.count()
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_doctor(request, doctor_id):
    """
    Get details of a specific doctor
    """
    doctor = get_object_or_404(Doctor, id=doctor_id)
    serializer = DoctorSerializer(doctor)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_doctor(request, doctor_id):
    """
    Update doctor details
    """
    doctor = get_object_or_404(Doctor, id=doctor_id, created_by=request.user)
    serializer = DoctorSerializer(doctor, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'Doctor updated successfully',
            'doctor': serializer.data
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_doctor(request, doctor_id):
    """
    Delete a doctor record
    """
    doctor = get_object_or_404(Doctor, id=doctor_id, created_by=request.user)
    doctor.delete()
    return Response({
        'message': 'Doctor deleted successfully'
    }, status=status.HTTP_200_OK)