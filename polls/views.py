from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse


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
