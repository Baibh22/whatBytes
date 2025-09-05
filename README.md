# Healthcare Backend System

A Django REST Framework backend for managing healthcare data with JWT authentication.

## Features

- **User Authentication**: JWT-based registration and login
- **Patient Management**: Complete CRUD operations
- **Doctor Management**: Complete CRUD operations  
- **Patient-Doctor Mapping**: Assign doctors to patients
- **Admin Interface**: Django admin for data management

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Superuser
```bash
python manage.py createsuperuser
```

### 4. Start Server
```bash
python manage.py runserver
```


## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register user
- `POST /api/auth/login/` - Login user
- `GET /api/auth/profile/` - Get user profile

### Patients
- `POST /api/patients/create/` - Create patient
- `GET /api/patients/` - List patients
- `GET /api/patients/{id}/` - Get patient
- `PUT /api/patients/{id}/update/` - Update patient
- `DELETE /api/patients/{id}/delete/` - Delete patient

### Doctors
- `POST /api/doctors/create/` - Create doctor
- `GET /api/doctors/` - List doctors
- `GET /api/doctors/{id}/` - Get doctor
- `PUT /api/doctors/{id}/update/` - Update doctor
- `DELETE /api/doctors/{id}/delete/` - Delete doctor

### Mappings
- `POST /api/mappings/create/` - Create mapping
- `GET /api/mappings/` - List mappings
- `GET /api/mappings/patient/{id}/` - Get patient doctors
- `PUT /api/mappings/{id}/update/` - Update mapping
- `DELETE /api/mappings/{id}/delete/` - Delete mapping

## Access Points

- **API Base**: http://localhost:8000/api/
- **Admin Panel**: http://localhost:8000/admin/
- **Demo Script**: `python demo.py`

## Technology Stack

- Django 4.2.7
- Django REST Framework 3.14.0
- Supabase PostgreSQL (Cloud)
- JWT Authentication
- Python 3.8+
