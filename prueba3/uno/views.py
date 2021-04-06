from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context

def suma(request, num1, num2):
    res = num1 + num2
    contenido = """
    <html>
        <head> </head>
        <body>
            <h1>El resultado es: %s </h1>
        </body>
    </html>
    """ %res
    return HttpResponse(contenido)

def prueba1 (request):
    externo = open("/Library/WebServer/Documents/Django/DjangoProjects/prueba3/Templates/prueba.html")
    plantilla = Template(externo.read())
    externo.close()
    ctx = Context()
    contenido = plantilla.render(ctx)
    


def prueba2 (request):
    return render (request, "prueba.html")

def graficaPrueba (request):    
    externo = open("/Library/WebServer/Documents/Django/DjangoProjects/prueba3/Templates/graficaPrueba.html")
    plantilla = Template(externo.read())
    externo.close()
    ctx = Context()
    contenido = plantilla.render(ctx)
    return HttpResponse(contenido)