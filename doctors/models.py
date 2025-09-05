from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Doctor(models.Model):
    """
    Doctor model to store doctor information
    """
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    # Basic Information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    
    # Professional Information
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)
    years_of_experience = models.PositiveIntegerField()
    education = models.TextField()
    hospital_affiliation = models.CharField(max_length=200, blank=True, null=True)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    # Availability
    is_available = models.BooleanField(default=True)
    working_hours = models.CharField(max_length=100, blank=True, null=True)
    
    # System Information
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_doctors')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"Dr. {self.first_name} {self.last_name}"

    class Meta:
        db_table = 'doctors'
        ordering = ['-created_at']