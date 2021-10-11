from django.contrib.auth import views
from django.urls import path
from accounts.views import register
from accounts.views import PasswordResetDone, PasswordResetComplete
from .views import info
from market.views import ShowCart

app_name = 'accounts'

urlpatterns = [
    path('cart/', ShowCart.as_view(), name='cart'),
    path('info/', info, name='info'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('reset_password/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDone, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetComplete, name='password_reset_complete'),
]
