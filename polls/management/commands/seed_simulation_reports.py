import random
from django.core.management.base import BaseCommand
from polls.models import SimulationReport

class Command(BaseCommand):
    help = 'Seed the database with mock data for SimulationReport'

    def handle(self, *args, **kwargs):
        # Clear existing data

        # Generate mock data
        vibration_levels = ['V1', 'V2', 'V3']

        for i in range(10):  # Create 10 mock entries
            # Generate random data points: time, frequency, and intensity
            data_points = [
                {
                    'time': round(random.uniform(0, 60), 2),  # Random time between 0 and 60 seconds
                    'frequency': round(random.uniform(50, 1000), 2),  # Frequency between 50 Hz and 1000 Hz
                    'intensity': round(random.uniform(1, 10), 2)  # Intensity between 1 and 10
                } for _ in range(5)  # Generate 5 data points
            ]

            frequency = random.uniform(50, 1000)  # Overall frequency between 50 Hz and 1000 Hz
            intensity = random.uniform(1, 10)  # Overall intensity between 1 and 10
            duration = random.uniform(10, 300)  # Duration between 10 and 300 seconds
            vibration_level = random.choice(vibration_levels)

            # Create and save the mock SimulationReport
            SimulationReport.objects.create(
                data_points=data_points,
                frequency=frequency,
                intensity=intensity,
                duration=duration,
                vibration_level=vibration_level
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with mock simulation reports'))
