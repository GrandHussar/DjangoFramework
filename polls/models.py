from django.db import models

# Create your models here.
class SimulationReport(models.Model):
    data_points = models.JSONField()  # Storing JSON data points
    frequency = models.FloatField()  # Frequency detected
    intensity = models.FloatField()  # Intensity detected
    duration = models.FloatField()  # Duration of the simulation in seconds
    VIBRATION_LEVEL_CHOICES = [
        ('V1', 'Vibration Level 1'),
        ('V2', 'Vibration Level 2'),
        ('V3', 'Vibration Level 3'),
    ]
    vibration_level = models.CharField(max_length=2, choices=VIBRATION_LEVEL_CHOICES)

    def __str__(self):
        return f"Simulation Report {self.id} - {self.vibration_level}"