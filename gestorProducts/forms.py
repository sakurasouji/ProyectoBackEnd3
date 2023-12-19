from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from gestorProducts.models import *


#______________________PRODUCTOS___________________________________#
class newProductForm(forms.Form):
    nombre = forms.CharField(label='Nombre Producto')
    precio = forms.IntegerField(label='Precio')
    descripcion = forms.CharField(label='Descripción Producto')
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
    
    nombre.widget.attrs['class'] = 'form-control'
    precio.widget.attrs['class'] = 'form-control'
    descripcion.widget.attrs['class'] = 'form-control'
    categoria.widget.attrs['class'] = 'form-control'
    
class newProductForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre Producto')
    precio = forms.IntegerField(label='Precio')
    descripcion = forms.CharField(label='Descripción Producto')
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
    
    nombre.widget.attrs['class'] = 'form-control'
    precio.widget.attrs['class'] = 'form-control'
    descripcion.widget.attrs['class'] = 'form-control'
    categoria.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Producto
        fields = (
            'nombre',
            'categoria',
            'precio',
            'descripcion'
            )
            
#__________________________CATEGORIAS_____________________________#    
class newCategoriaForm(forms.Form):
    nombre = forms.CharField(label='Nombre Categoría')
    descripcion = forms.CharField(label='Descripción Categoria')
    
class newCategoriaForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre Categoría')
    descripcion = forms.CharField(label='Descripción Categoria')   
    
    class Meta:
        model = Categoria
        fields = '__all__'
        
