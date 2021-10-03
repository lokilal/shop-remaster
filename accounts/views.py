from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib import messages


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

