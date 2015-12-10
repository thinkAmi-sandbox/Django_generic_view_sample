from django.shortcuts import render
from django.template.response import TemplateResponse

def register(request):
    return TemplateResponse(request, 'create_view.html', {})

# Create your views here.
