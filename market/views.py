from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category, Item


class Index(ListView):
    model = Item
    paginate_by = 10
    template_name = 'market/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class DetailsPage(DetailView):
    template_name = 'market/detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Item, slug=self.kwargs['slug'])
