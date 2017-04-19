from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, "homepages/index.html")
# Create your views here.
