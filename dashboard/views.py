from django.shortcuts import render
from . models import CountryData
# import json
# Create your views here.
def index(request):
    data = CountryData.objects.all()
    return render(request, 'index.html', {'data': data})