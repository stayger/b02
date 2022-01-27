import json
from django.shortcuts import render
from django.db.models import *
from django.template import context
from .models import Conc


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

def add(request):
    return render(request, 'main/add.html')


def add_conc(request):
    month = request.POST["month"]
    data = json.loads(request.POST["data1"])
    for item in data:
        print(item)
    
    context = {'month': month, 'data':data}
    return render(request, 'main/add_conc.html',context=context)


def report(request):
    month = '1'
    if request.method == 'POST':
        month = request.POST['month']



    items = Conc.objects.filter(dt__month=month) \
        .aggregate(Min('fe'), Max('fe'), Avg('fe'),
                   Min('si'), Max('si'), Avg('si'),
                   Min('al'), Max('al'), Avg('al'),
                   Min('ca'), Max('ca'), Avg('ca'),
                   Min('s'), Max('s'), Avg('s'),
                   )
    months = range(1, 13)
    return render(request, 'main/report.html', {'items': items, 'months': months, 'mm': month})
