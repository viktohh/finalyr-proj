from django.shortcuts import render
from django.contrib import messages

def index(request):
    context = {
        "page_title": "Welcome to Online Assignment System"
    }
    return render(request, 'assignments/index.html', context)