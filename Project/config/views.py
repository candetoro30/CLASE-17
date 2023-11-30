from django.http import HttpResponse
# from django.template import Context, Template
from datetime import datetime
from django.shortcuts import render

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def saludo_vista(request):
    return HttpResponse("<h1>Segunda vista</h2>")
    
def nombre(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    edad = input("Ingresa tu edad: ")
    return HttpResponse(f"{apellido}, {nombre}: edad {edad}")


# def probando_template(request):
#     mi_html = open("./templates/template1.html")
#     mi_template = Template(mi_html.read())
#     mi_html.close()
#     nombre = "Candelaria"
#     apellido = "Toro"
#     ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#     datos = {"nombre": nombre, "apellido": apellido, "fecha": ahora}
#     mi_contexto = Context(datos)
#     mi_documento = mi_template.render(mi_contexto)
#     return HttpResponse(mi_documento)

def probando_template(request):
    nombre = "Candelaria"
    apellido = "Toro"
    ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    datos = {"nombre": nombre, "apellido": apellido} #CONTEXTO
    datos["fecha"] = ahora
    return render(request, "template1.html", datos)

def mis_notas(request):
    lista_de_notas = [2, 3, 5, 9]
    contexto = {"notas": lista_de_notas}
    return render(request, "notas.html", contexto)

def diccionario(request):
    mi_diccionario = {"colores": {"rojo": "red", "azul": "blue", "verde": "green"}}
    return render(request, "template2.html", mi_diccionario)