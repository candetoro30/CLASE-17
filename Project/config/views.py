from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def saludo_vista(request):
    return HttpResponse("<h1>Segunda vista</h2>")
    