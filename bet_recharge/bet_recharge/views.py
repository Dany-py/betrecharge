from django.http import HttpResponse
#from django.shortcuts import render




def page(request):
    return HttpResponse("<h1>Bonjour tous le monde</h1>")