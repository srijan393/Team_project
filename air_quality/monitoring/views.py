# monitoring/views.py

from django.shortcuts import render, redirect
from .models import AirQualityData
from .forms import AirQualityDataForm


def air_quality_list(request):
    # Get all air quality data from the database
    data = AirQualityData.objects.all()

    # Initialize the form for creating new data
    if request.method == 'POST':
        form = AirQualityDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('air_quality_list')  # Redirect after saving
    else:
        form = AirQualityDataForm()

    # Extract data for chart
    timestamps = [entry.timestamp.strftime('%Y-%m-%d %H:%M:%S') for entry in data]
    temperature_data = [entry.temperature for entry in data]
    humidity_data = [entry.humidity for entry in data]
    air_quality_data = [entry.air_quality for entry in data]

    # Pass data to the template
    return render(request, 'monitoring/air_quality_list.html', {
        'data': data,
        'form': form,
        'data_temperature': temperature_data,
        'data_humidity': humidity_data,
        'data_air_quality': air_quality_data,
        'data_timestamps': timestamps
    })


def view_data(request):
    # This view will show the air quality data
    data = AirQualityData.objects.all()

    # You can customize this view if needed
    return render(request, 'monitoring/air_quality_list.html', {'data': data})
def view_data(request):
    data = AirQualityData.objects.all()  # Fetch all the data from the database
    return render(request, 'monitoring/view_data.html', {'data': data})