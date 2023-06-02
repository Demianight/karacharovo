from django.shortcuts import render
from django.http import HttpRequest
from .models import Title


def index(request: HttpRequest):
    titles = Title.objects.all()
    context = {
        'titles': titles
    }
    return render(request, 'index.html', context)
