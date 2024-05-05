from django.shortcuts import render
from .models import Patient

def display_patients(request):
    patients = Patient.objects.all()
    return render(request, 'myapp/display_patient.html', {'patients': patients})