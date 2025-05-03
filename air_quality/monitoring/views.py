# monitoring/views.py

from django.shortcuts import render, redirect
from .models import AirQualityData
from .forms import AirQualityDataForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

@login_required
@csrf_protect
def clear_air_quality_data(request):
    if request.method == 'POST':
        AirQualityData.objects.all().delete()
        messages.success(request, "All air quality data has been cleared.")
    return redirect('air_quality_list')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid login credentials')
    else:
        form = AuthenticationForm()
    return render(request, 'monitoring/login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('view_data')
        else:
            messages.error(request, 'Signup failed. Try again.')
    else:
        form = UserCreationForm()
    return render(request, 'monitoring/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def about_view(request):
    return render(request, 'monitoring/about.html')


@login_required
def air_quality_list(request):
    data = AirQualityData.objects.all()

    if request.method == 'POST':
        form = AirQualityDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('air_quality_list')
    else:
        form = AirQualityDataForm()

    timestamps = [entry.timestamp.strftime('%Y-%m-%d %H:%M:%S') for entry in data]
    temperature_data = [entry.temperature for entry in data]
    humidity_data = [entry.humidity for entry in data]
    air_quality_data = [entry.air_quality for entry in data]

    return render(request, 'monitoring/air_quality_list.html', {
        'data': data,
        'form': form,
        'data_temperature': temperature_data,
        'data_humidity': humidity_data,
        'data_air_quality': air_quality_data,
        'data_timestamps': timestamps
    })


@login_required
def view_data(request):
    data = AirQualityData.objects.all()
    return render(request, 'monitoring/view_data.html', {'data': data})
