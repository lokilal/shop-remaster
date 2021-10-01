from django.shortcuts import render, HttpResponse
from django.shortcuts import  get_object_or_404
from django.views.generic.list import ListView
from .models import Category, Item


def index(request):
    print(Category.objects.last().slug)
    return HttpResponse('dsa')


class Index(ListView):
    model = Item
    paginate_by = 10
    template_name = 'market/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context
