import random
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from polls.models import Simulation, SimulationResult

class Command(BaseCommand):
    help = 'Seed the database with mock data for SimulationResult'

    def handle(self, *args, **kwargs):
        # Clear existing data (optional)
        SimulationResult.objects.all().delete()
        Simulation.objects.all().delete()

        # Fetch existing users from the database
        users = list(User.objects.all())
        
        # If no users exist, create some mock users
        if not users:
            users = [
                User.objects.create_user(username=f'user{i}', password='password')
                for i in range(3)
            ]

        # Generate mock simulations and associate with users
        simulations = [
            Simulation.objects.create(user=random.choice(users))  # Ensure a valid user is assigned
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
            SimulationResult.objects.create(
                simulation=simulation,
                user=user,  # Ensure a valid user is assigned
                data_points=data_points,
                frequency=frequency,
                intensity=intensity,
                duration=duration,  # Set duration
                vibration_level=vibration_level
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with mock simulation results'))
