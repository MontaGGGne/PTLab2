from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import Product, Purchase

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)


class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['product', 'product_quantity', 'person', 'address']

    def form_valid(self, form):
        self.object = form.save()
        product_quantity = self.object.product_quantity
        print(f"product_quantity - {product_quantity}")
        product_id = self.object.product_id
        print(f"product_id - {product_id}")
        try:
            product = Product.objects.filter(id=product_id).first()
        except Exception as e:
            print(repr(e))
            exit(0)
        # product = Product.from_db
        print(f"product - {product}")
        try:
            pq = product.quantity
        except Exception as e:
            print(repr(e))
            exit(0)
        print(f"product.quantity before - {product.quantity}")
        product.quantity = product.quantity - product_quantity
        print(f"product.quantity - {product.quantity}")
        product.save()
        return HttpResponse(f'Спасибо за покупку, {self.object.person}!')

