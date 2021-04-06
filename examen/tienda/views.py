from django.shortcuts import render, HttpResponse
from tienda.models import Prendas
# Create your views here.
def inicio(request):
    articulos= Prendas.objects.all()
    return render(request,"index.html",{"articulos":articulos})