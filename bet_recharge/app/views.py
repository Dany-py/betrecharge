from django.shortcuts import render

# Create your views here.

def paage(request):
    return render(request, "page1.html")