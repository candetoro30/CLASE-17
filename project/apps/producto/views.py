from django.shortcuts import render

# Create your views here.
def home(request):
    contexto = {"app": "Aplicacion producto"}
    return render(request, "producto/index.html", contexto)
    

