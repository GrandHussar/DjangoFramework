from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import SimulationResult
from .serializers import SimulationResultSerializer
from django.views.decorators.csrf import ensure_csrf_cookie

import os

class SimulationReportViewSet(viewsets.ModelViewSet):
    queryset = SimulationResult.objects.all().order_by('id')
    serializer_class = SimulationResultSerializer

# API views
@api_view(['GET'])
def sample_api(request):
    return Response({"message": "Hello from sample API!"})

@api_view(['GET'])
def get_data(request):
    data = {
        'message': 'This is a sample JSON response',
        'data': [1, 2, 3, 4]
    }
    return Response(data)

# Serve React App for main routes
def index(request):
    return render(request, 'index.html')  # Loads React's index.html

def dashboard(request):
    return render(request, 'index.html')  # Loads React's index.html for the dashboard view
def login(request):
    return render(request, 'index.html')  # Loads React's index.html for the dashboard view

def settings(request):
    return render(request, 'index.html')  # Loads React's index.html for the dashboard view

def reports(request):
    return render(request, 'index.html')  # Loads React's index.html for the dashboard view

def welcome(request):
    return render(request, 'index.html')  # Loads React's index.html for the welcome view

def update_simulation(request):
    if request.method == 'POST':
        frequency = request.POST.get('frequency')
        amplitude = request.POST.get('amplitude')
        print(f"Updated Frequency: {frequency} Hz")
        print(f"Updated Amplitude: {amplitude} ms²")
    return redirect('dashboard')
import random
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from polls.models import Simulation, SimulationResult  # Import MongoEngine models

class Command(BaseCommand):
    help = 'Seed the database with mock data for SimulationResult'

    def handle(self, *args, **kwargs):
        # Clear existing data (optional)
        SimulationResult.objects.delete()
        Simulation.objects.delete()

        # Fetch existing users from the database
        users = list(User.objects.all())
        
        # If no users exist, create some mock users
        if not users:
            users = [
                User.objects.create_user(username=f'user{i}', password='password')
                for i in range(3)
            ]

        # Generate mock simulations and associate them with users
        simulations = [
            Simulation(user_id=random.choice(users).id, status="running").save()
            for _ in range(5)
        ]

        vibration_levels = ['V1', 'V2', 'V3']

        for i in range(10):  # Create 10 mock entries for SimulationResult
            # Choose a random duration: either 2 hours (7200 seconds) or 20 hours (72000 seconds)
            duration = random.choice([7200, 72000])

            # Generate data points for each second of the simulation
            data_points = [
                {
                    'time': second,  # Time is each second
                    'frequency': round(random.uniform(0, 60), 2),  # Frequency between 0 and 60 Hz
                    'intensity': round(random.uniform(30, 60), 2)  # Acceleration between 30 and 60 m/s²
                } for second in range(duration)  # Generate data points for every second of the simulation
            ]

            # Choose random overall values
            frequency = round(random.uniform(0, 60), 2)  # Overall frequency between 0 and 60 Hz
            intensity = round(random.uniform(30, 60), 2)  # Overall acceleration between 30 and 60 m/s²
            vibration_level = random.choice(vibration_levels)

            # Associate each result with a random Simulation and User
            simulation = random.choice(simulations)
            user = random.choice(users)

            # Create and save the mock SimulationResult
            SimulationResult(
                simulation=simulation,
                user_id=user.id,  # Store the user ID as integer
                data_points=data_points,
                frequency=frequency,
                intensity=intensity,
                duration=duration,  # Set duration
                vibration_level=vibration_level
            ).save()

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with mock simulation results'))

@ensure_csrf_cookie
def csrf_token_view(request):
    return JsonResponse({"message": "CSRF cookie set"})
