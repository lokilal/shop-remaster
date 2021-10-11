from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic.list import ListView
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.models import CartItem
from market.models import Item


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')

    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def PasswordResetDone(request):
    if request.method == 'GET':
        messages.success(request, "Проверьте почту")
        return redirect('market:index')
    return redirect('market:index')


def PasswordResetComplete(request):
    if request.method == 'GET':
        messages.success(request, 'Пароль успешно изменен.')
        return redirect('accounts:login')
    return redirect('accounts:login')


@login_required()
def info(request):
    return render(request, 'market/profile.html')

