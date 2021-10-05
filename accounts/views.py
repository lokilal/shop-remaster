from django.http import HttpResponse
from django.views.generic.list import ListView
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib import messages
from accounts.models import Cart, CartItem
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


def info(request):
    return HttpResponse(f'Это профиль {request.user.username}')


def showCart(requset):
    return HttpResponse(f"Это корзина пользователя {requset.user.username}")


class ShowCart(ListView):
    template_name = 'market/cart.html'
    model = Item

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user.username)

