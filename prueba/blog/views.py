from django.shortcuts import render, HttpResponse
from blog.models import Articulo
# Create your views here.
def inicio(request):
    articulos=Articulo.objects.all
    return render(request,"home.html",{"articulos":articulos})