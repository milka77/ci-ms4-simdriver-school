from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm

# Create your views here.


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HAtaMLXFpruDvBntY9jHWkbbTmXV9AMQQdhLd6sSIUeerYb1Fyd7yi8qEyAV3YH6PFIDzDvtlhbuQlJr2yeUsyT00RaOcrzkL',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
