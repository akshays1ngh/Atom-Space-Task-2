# myapp/urls.py
from django.urls import path
from .views import display_patient

urlpatterns = [
    # ... your existing URL patterns ...
    path('display-patient/', display_patients, name='display_patient'),
]