from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category, Item
from django.contrib import messages
from accounts.models import Cart, CartItem


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

    def post(self, request, *args, **kwargs):
        amount = int(request.POST['qtybutton'])
        product = self.get_object()
        if len(CartItem.objects.filter(cart=request.user.pk)) == 0:
            Cart.objects.create(user=request.user.username)
            user_cart = Cart.objects.get(user=request.user.username)
            CartItem.objects.create(product=Item.objects.get(pk=product.pk),
                                    quantity=amount,
                                    price=product.price,
                                    cart=user_cart)
        else:
            user_cart = Cart.objects.get(user=request.user.username)
            if len(CartItem.objects.filter(cart=request.user.pk,
                                           product=Item.objects.get(pk=product.pk))) == 0:
                CartItem.objects.create(product=Item.objects.get(pk=product.pk),
                                        quantity=amount,
                                        price=product.price,
                                        cart=user_cart)
            else:
                last_amount = CartItem.objects.filter(cart=request.user.pk,
                                                      product=Item.objects.get(pk=product.pk))[0].quantity
                CartItem.objects.filter(cart=request.user.pk,
                                        product=Item.objects.get(pk=product.pk)).update(quantity=last_amount + amount)
        messages.success(request, 'Успешно добавлено в корзину')
        return redirect('market:index')
