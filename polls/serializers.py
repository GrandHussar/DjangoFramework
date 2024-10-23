from rest_framework import serializers
from .models import SimulationReport

class SimulationReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimulationReport
        fields = '__all__'
