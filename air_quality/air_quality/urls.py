# air_quality/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('monitoring/', include('monitoring.urls')),  # Include the monitoring app URLs
    path('', include('monitoring.urls')),  # Redirect the root URL to the monitoring app
]
