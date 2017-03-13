from django.shortcuts import render
from django.http import HttpResponse
from brad.models import Brad
from datetime import datetime

# Create your views here.
def home(request):
    post_list=Brad.objects.all()
    return render(request,'test3.html',{'post_list':post_list})

# def home(request):
#     return HttpResponse("Hello World, Brad")

# def detail(request,my_args):
#     return HttpResponse("you're looking at my_args: %s"%my_args)
#
# def test(request):
#     return render(request,'test.html',{'current_time':datetime.now()})