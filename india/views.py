from django.shortcuts import render

# Create your views here.

def dhoni(request):
    return render(request,'dhoni.html')

def virat(request):
    return render(request,'virat.html')