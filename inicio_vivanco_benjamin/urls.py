from django.urls import path
from . import views

# Configuración de namespace
app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='home'),
    path('tema/<int:tema_id>/', views.detalle_tema, name='detalle_tema'),
]
