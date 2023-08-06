from django.shortcuts import render,redirect,get_object_or_404

from . import models
from . import forms
from django.contrib.auth.decorators import login_required
# Create your views here.

def ListadoProductos(request):
    productos = models.TablaProductos.objects.all().order_by('id')
    categorias = models.Categoria.objects.all()
    formularioProductos = forms.ProductoFrom()
    ctx = {'productos':productos,'categorias':categorias,'formulario':formularioProductos}
    
    return render(request,'listado.html',ctx)
@login_required
def CrearProducto(request):
    formularioProducto = forms.ProductoFrom(request.POST)
    if formularioProducto.is_valid():
        formularioProducto.save()
        return redirect('listado')
    
@login_required   
def EliminarProducto(request,id_producto):
    producto = models.TablaProductos.objects.get(id=id_producto)
    producto.delete()
    return redirect('listado')

@login_required
def EditarProducto(request,id_producto):       
    producto = get_object_or_404(models.TablaProductos,id=id_producto)
    if request.method == 'GET':
        formularioProducto = forms.ProductoFrom(instance=producto)
        ctx = {'formulario':formularioProducto,'producto':producto}
        return render(request,"editar.html",ctx)
    elif request.method == 'POST': 
        formularioProducto = forms.ProductoFrom(request.POST,instance=producto)
        if formularioProducto.is_valid():
            formularioProducto.save()
            
        return redirect('listado')

