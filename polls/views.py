from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import SimulationReport
from .serializers import SimulationReportSerializer

class SimulationReportViewSet(viewsets.ModelViewSet):
    queryset = SimulationReport.objects.all().order_by('id')
    serializer_class = SimulationReportSerializer

# Define the sample_api view
@api_view(['GET'])
def sample_api(request):
    return Response({"message": "Hello from sample API!"})

# Define the get_data view
@api_view(['GET'])
def get_data(request):
    # Sample data to return as JSON
    data = {
        'message': 'This is a sample JSON response',
        'data': [1, 2, 3, 4]
    }
    return Response(data)

def index(request):
    return HttpResponse("Django Test One")

def welcome(request):
    return render(request, 'polls/welcome.html')

def dashboard(request):
    return render(request, 'polls/dashboard.html')

def update_simulation(request):
    if request.method == 'POST':
        frequency = request.POST.get('frequency')
        amplitude = request.POST.get('amplitude')
        # Here you can handle the data (e.g., update simulation parameters)
        print(f"Updated Frequency: {frequency} Hz")
        print(f"Updated Amplitude: {amplitude} ms²")
    return redirect('dashboard')
