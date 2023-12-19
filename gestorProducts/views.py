from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from gestorProducts.models import *
from .forms import newProductForm, newCategoriaForm
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def is_admin(user):
    return user.is_superuser

def is_not_admin(user):
    value = not(user.is_superuser)
    return value


def createProduct(request):
    if request.method == "POST":
        form = newProductForm(request.POST, request.FILES)
        if form.is_valid():   
            instance = form.save(commit=False)
            instance.autor = request.user
            instance.save()
            form.save()
            form.cleaned_data['nombre'] = ''
            form.cleaned_data['descripcion'] = ''
            form.cleaned_data['precio'] = ''
            form.cleaned_data['categoria'] = ''
            print("Producto agregado correctamente")
            return HttpResponseRedirect(reverse('dashboard'))
            
    else:
        form = newProductForm()        
    data = {'form': form,
            'titulo_menu': 'Crear Producto',
            'boton': 'Crear Producto'
            }
    return render(request, 'gestorProducts/createProduct.html', data)

@user_passes_test(is_admin)
def createCategoria(request):
    if request.method == "POST":
        form = newCategoriaForm(request.POST, request.FILES)
        if form.is_valid():   
            print("Categoría agregada correctamente")
            form.save()
            form.cleaned_data['nombre'] = ''
            form.cleaned_data['descripcion'] = ''
            print("Producto agregado correctamente")
            return HttpResponseRedirect(reverse('dashboard'))
            
    else:
        form = newCategoriaForm()        
    data = {'form': form,
            'titulo_menu': 'Crear Categoria',
            'boton': 'Crear Categoria'}
    return render(request, 'gestorProducts/createCategoria.html', data)

@user_passes_test(is_admin)
def readProducts(request):
    products = Producto.objects.all()
    data = {
        'products' : products
    }
    return render(request, 'gestorProducts/listaProductos.html', data)

@user_passes_test(is_not_admin)
def readProductsUser(request):
    current_user = request.user
    products = Producto.objects.filter(autor_id = current_user.id)
    data = {
        'products' : products
    }
    return render(request, 'gestorProducts/listaProductosUser.html', data)

@user_passes_test(is_admin)
def readCategorias(request):
    categorias = Categoria.objects.all()
    data = {
        'categorias' : categorias
    }
    return render(request, 'gestorProducts/listaCategorias.html', data)


def editProduct(request, id):
    product = Producto.objects.get(id = id)
    form = newProductForm(instance=product)
    if request.method == "POST":
        form = newProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            if request.user.is_superuser:
                return HttpResponseRedirect(reverse('listaProductos'))
            else:
                return HttpResponseRedirect(reverse('listaProductosUser'))                 
    data = {'form': form,
            'titulo' : 'Editar Producto',
            'boton' : 'Aplicar cambios'
            }
    return render(request, 'gestorProducts/createProduct.html', data)

@user_passes_test(is_admin)
def delProduct(request, id):
    prod = Producto.objects.get(id = id)
    prod.delete()
    return HttpResponseRedirect(reverse('listaProductos'))

@user_passes_test(is_admin)
def editCategoria(request, id):
    categoria = Categoria.objects.get(id = id)
    form = newCategoriaForm(instance=categoria)
    if request.method == "POST":
        form = newCategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listaCategorias'))                 
    data = {'form': form,
            'titulo' : 'Editar Categoria',
            'boton' : 'Aplicar cambios'
            }
    return render(request, 'gestorProducts/createProduct.html', data)

@user_passes_test(is_admin)
def delCat(request, id):
    cat = Categoria.objects.get(id = id)
    cat.delete()
    return HttpResponseRedirect(reverse('listaCategorias'))