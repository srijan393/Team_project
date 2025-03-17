# monitoring/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.air_quality_list, name='air_quality_list'),
    path('view_data/', views.view_data, name='view_data'),  # Make sure 'view_data' is here
]
