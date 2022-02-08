from django.shortcuts import render, redirect, reverse

# Create your views here.
def index(request):

    if request.method == "GET":
        return render(request, 'camion/index.html')

    if request.method == "POST":
        print(request.POST)
        # PROCESAR EN BASE DE DATOS
        nombre = request.POST.get('nombre',None)
        apellido = request.POST['apellido']

        print("A LA BASE DE DATOS:" + nombre + " " + apellido)

        contexto = {
            'nombre': nombre,
            'apellido': apellido,
            'tipo' : request.POST.get('tipo', 'normal')
        }

        request.session['usuario'] = contexto

        return redirect( reverse('camion:success') )

def resultados(request):
    return render(request, 'camion/resultados.html')