from django.shortcuts import render
from django.http import HttpResponse
import random 

def index (request):
    contenido = """
        <html>
            <head>
                <title>Reloj</title>
            </head>
            <body>
                <h1>Hola Mundo</h1>

            </body>
        </html>
    """
    return HttpResponse(contenido)

def suma (request):

    num1 = random.choice (range(100))
    num2 = random.choice (range(100))
    print ("Numero 1: ",num1)
    print ("Numero 2: ",num2)
    suma = num1 + num2
    print ("El resultado es: ", suma)
    
    return HttpResponse("Numero 1: %s /n Numero 2: %s" %num1 %num2)
    

