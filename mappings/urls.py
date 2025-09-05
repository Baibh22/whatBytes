from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_mappings, name='list_mappings'),
    path('create/', views.create_mapping, name='create_mapping'),
    path('patient/<int:patient_id>/', views.get_patient_doctors, name='get_patient_doctors'),
    path('<int:mapping_id>/update/', views.update_mapping, name='update_mapping'),
    path('<int:mapping_id>/delete/', views.delete_mapping, name='delete_mapping'),
]
