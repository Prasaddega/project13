from django.shortcuts import render

# Create your views here.

def smith(request):
    return render(request,'smith.html')

def warner(request):
    return render(request,'warner.html')