from django.http import Http404
from django.shortcuts import render
from .models import Camera


def get_cameras(request):
    return render(request, 'camera.html', {'cameras': Camera.objects.all()})
