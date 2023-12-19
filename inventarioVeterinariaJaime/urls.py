"""
URL configuration for inventarioVeterinariaJaime project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gestorUser.views import *
from gestorProducts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),    
    path('dashboard/', userIndex, name="dashboard"),
    path('signUp/', signUp, name='signUp'),
    path('addProduct/', createProduct, name='addProduct'),
    path('addCategoria/', createCategoria, name='addCategoria'),
    path('listaProductos/', readProducts, name='listaProductos'),
    path('listaCategorias/', readCategorias, name='listaCategorias'),
    path('listaUsuarios/', readUsers, name='listaUsuarios'),
    path('editUser/<int:id>', editUser, name='editUser'),
    path('delUser/<int:id>', delUser, name='delUser'),
    path('editProduct/<int:id>', editProduct, name='editProduct'),
    path('editCategoria/<int:id>', editCategoria, name='editCategoria'),
    path('delCat/<int:id>', delCat, name='delCat'),
    path('delProduct/<int:id>', delProduct, name='delProduct'),
    path('listaProductosUser/', readProductsUser, name='listaProductosUser'),
    
    
]
