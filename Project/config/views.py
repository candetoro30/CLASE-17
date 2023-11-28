from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def saludo_vista(request):
    return HttpResponse("<h1>Segunda vista</h2>")
    
def nombre(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    edad = input("Ingresa tu edad: ")
    return HttpResponse(f"{apellido}, {nombre}: edad {edad}")



