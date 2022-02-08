import re
from django.shortcuts import render, redirect

# Create your views here.
def index(request):

    if request.method == "GET":
        return render(request, 'app/index.html')

    if request.method == "POST":
        print(request.POST)
        # PROCESAR EN BASE DE DATOS
        return redirect("/")