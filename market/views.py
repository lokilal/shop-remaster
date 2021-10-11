from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category, Item
from django.contrib import messages
from accounts.models import Cart, CartItem

session_cart = SessionStore()
session_cart.create()
session_cart = SessionStore(session_key=session_cart.session_key)


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
        if request.user.is_authenticated:
            """Если пользователь авторизован"""
            if len(Cart.objects.filter(user=request.user.username)) == 0:
                """Если корзины не существовало, то создадим ее"""
                Cart.objects.create(user=request.user.username)
                user_cart = Cart.objects.get(user=request.user.username)
                CartItem.objects.create(product=Item.objects.get(pk=product.pk),
                                        quantity=amount,
                                        price=product.price,
                                        cart=user_cart)
            else:
                """Если корзина уже создана"""
                user_cart = Cart.objects.get(user=request.user.username)
                if len(CartItem.objects.filter(cart__user=request.user.username,
                                               product=Item.objects.get(pk=product.pk))) == 0:
                    """Если товара нет в корзине"""
                    CartItem.objects.create(product=Item.objects.get(pk=product.pk),
                                            quantity=amount,
                                            price=product.price,
                                            cart=user_cart)
                else:
                    """Если товар в корзине, нужно добавить к количеству"""
                    last_amount = CartItem.objects.filter(cart__user=request.user.username,
                                                          product=Item.objects.get(pk=product.pk))[0].quantity
                    CartItem.objects.filter(cart__user=request.user.username,
                                            product=Item.objects.get(pk=product.pk)).update(
                                            quantity=last_amount + amount)
        else:
            """Если пользователь не авторизован, то нужно создать временную сессию,
             в которой будет храниться корзина"""
            if 'cart' in session_cart:
                """Если корзина уже создана, то нужно проверить наличие товара в ней"""
                item = Item.objects.get(pk=product.pk)
                if item in session_cart['cart']:
                    session_cart['cart'][item] += amount
                else:
                    session_cart['cart'][Item.objects.get(pk=product.pk)] = amount
            else:
                """Если корзина не создна, то создадим ее"""
                session_cart['cart'] = {}
                session_cart['cart'][Item.objects.get(pk=product.pk)] = amount
        messages.success(request, 'Успешно добавлено в корзину')
        return redirect('market:index')


class ShowCart(ListView):
    template_name = 'market/cart.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowCart, self).get_context_data(**kwargs)
        amount = 0
        for item, quantity in self.get_queryset().items():
            amount += item.price * quantity
        context['total_price'] = amount
        return context

    def get_queryset(self):
        if self.request.user.is_authenticated:
            items = CartItem.objects.filter(cart__user=self.request.user.username)
            queryset = {}
            for item in items:
                queryset[item.product] = item.quantity
        else:
            queryset = session_cart['cart']
        return queryset

    def post(self, request, *args, **kwargs):
        pk_delete = int(request.POST['delFromCart'])
        if self.request.user.is_authenticated:
            CartItem.objects.filter(cart__user=self.request.user.username)[pk_delete].delete()
        else:
            for index, item in enumerate(session_cart['cart']):
                if index == pk_delete:
                    del session_cart['cart'][item]
                    break
        return redirect('accounts:cart')

