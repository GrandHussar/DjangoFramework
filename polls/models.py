from django.db import models
from django.contrib.auth.models import User  # Using Django's default User model (auth_user)


# Simulation Model
class Simulation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key to auth_user table
    status = models.CharField(max_length=100)  # Status of the simulation (running, completed, etc.)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation

    def __str__(self):
        return f"Simulation {self.id} - User {self.user.id} - Status {self.status}"


# SimulationResult Model
class SimulationResult(models.Model):
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE)  # Foreign key to Simulation
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key to auth_user table
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
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation

    def __str__(self):
        return f"Simulation Result {self.id} - Simulation {self.simulation.id} - Vibration Level {self.vibration_level}"


# Control Model
class Control(models.Model):
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE)  # Foreign key to Simulation
    data_points = models.JSONField()  # Storing JSON data points
    frequency = models.FloatField()  # Frequency for control
    intensity = models.FloatField()  # Intensity of the vibration
    duration = models.FloatField()  # Duration of the control in seconds
    vibration_level = models.CharField(max_length=2, choices=[('V1', 'Level 1'), ('V2', 'Level 2')])
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation

    def __str__(self):
        return f"Control {self.id} - Simulation {self.simulation.id}"


# Sensor Model
class Sensor(models.Model):
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE)  # Foreign key to Simulation table
    data_points = models.JSONField()  # JSON field for sensor data points
    frequency = models.FloatField()  # Frequency recorded by the sensor
    intensity = models.FloatField()  # Intensity recorded by the sensor
    duration = models.FloatField()  # Duration of the recording
    vibration_level = models.CharField(max_length=2, choices=[('V1', 'Level 1'), ('V2', 'Level 2')])
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation

    def __str__(self):
        return f"Sensor {self.id} - Simulation {self.simulation.id} - Vibration Level {self.vibration_level}"