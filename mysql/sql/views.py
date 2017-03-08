from django.shortcuts import render
from .models import fruit
from django.http import HttpResponse

# Create your views here.
def query(request):
    output=fruit.objects.filter(id=1)
    p=output.name
    return HttpResponse(p)
