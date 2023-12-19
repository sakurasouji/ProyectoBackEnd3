from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from .forms import signUpForm
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def is_admin(user):
    return user.is_superuser
        

@login_required
def userIndex(request):
    if request.user.is_superuser:
        return render(request, 'gestorUser/dashboard.html')
    elif request.user.is_staff:
        return render(request, 'gestorUser/dashboard.html')
    else:
        return render(request, 'gestorUser/dashboardLite.html')
    
def signUp(request):
    usuario = Usuario
    
    form = signUpForm
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            if request.user.is_authenticated:
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                return HttpResponseRedirect(reverse('home'))
    
    return render(request, 'gestorUser/signUp.html', {'form': form})

@user_passes_test(is_admin)
def readUsers(request):
    users = User.objects.all()
    data = {
        'users' : users
    }
    return render(request, 'gestorUser/listaUsuarios.html', data)

def home(request):
    return render(request, 'home.html')

@user_passes_test(is_admin)
def editUser(request, id):
    user = User.objects.get(id = id)
    form = signUpForm(instance=user)
    if (request.method == 'POST'):
        form = signUpForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('listaUsuarios'))
    data = {'form' : form}
    return render(request, 'gestorUser/editUser.html', data)


@user_passes_test(is_admin)
def delUser(request, id):
    user = User.objects.get(id = id)
    user.delete()
    return HttpResponseRedirect(reverse('listaUsuarios'))