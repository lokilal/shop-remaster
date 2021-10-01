from django.urls import path
from . import views


app_name = 'market'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<slug:slug_category>/<slug:slug>/', views.DetailsPage.as_view(), name='detail'),
]
