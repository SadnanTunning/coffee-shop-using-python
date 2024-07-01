from django.shortcuts import render
from django.http import HttpResponse
from .models import Coffee

def home(request):
    try:
        coffee = Coffee.objects.all()
        return render(request, 'home.html', {'coffee': coffee})
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")
