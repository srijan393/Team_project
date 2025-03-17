# monitoring/forms.py

from django import forms
from .models import AirQualityData

class AirQualityDataForm(forms.ModelForm):
    class Meta:
        model = AirQualityData
        fields = ['temperature', 'humidity', 'air_quality']
        widgets = {
            'temperature': forms.NumberInput(attrs={'class': 'form-control'}),
            'humidity': forms.NumberInput(attrs={'class': 'form-control'}),
            'air_quality': forms.NumberInput(attrs={'class': 'form-control'}),
        }
