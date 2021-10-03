from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Введите логин', min_length=4, max_length=150)
    name = forms.CharField(label='Введите ФИО', min_length=4, max_length=150)
    email = forms.EmailField(label='Введите email')
    password1 = forms.CharField(label='Введите пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)
    mobile = forms.CharField(label='Введите телефон', min_length=4, max_length=150)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Пользователь с таким именем уже существует.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email уже зарегистрирован.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
            first_name=self.cleaned_data['name'],
            last_name=self.cleaned_data['mobile'],
        )
        return user
