from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category, Item


class Index(ListView):
    model = Item
    paginate_by = 25
    template_name = 'market/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class CategoryItems(Index):
    def get_queryset(self):
        category = get_list_or_404(Item, slug_category=self.kwargs['slug_category'])
        return category


class DetailsPage(DetailView):
    template_name = 'market/detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Item, slug=self.kwargs['slug'])
