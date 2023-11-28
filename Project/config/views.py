from django.http import HttpResponse
from django.template import Context, Template

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def saludo_vista(request):
    return HttpResponse("<h1>Segunda vista</h2>")
    
def nombre(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    edad = input("Ingresa tu edad: ")
    return HttpResponse(f"{apellido}, {nombre}: edad {edad}")


def probando_template(request):
    mi_html = open("./templates/template1.html")
    mi_template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context()
    mi_documento = mi_template.render(mi_contexto)
    return HttpResponse(mi_documento)

