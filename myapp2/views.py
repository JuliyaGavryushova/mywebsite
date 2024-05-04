from django.shortcuts import render, redirect, get_object_or_404
import logging
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from .models import Order, Product
from .forms import ProductForm

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'myapp2/base.html')


def products_ordered_by_customer(request, client_id, time_period):
    today = timezone.now()
    start_date = today - timezone.timedelta(days=time_period)

    orders = Order.objects.filter(customer_id=client_id, date_ordered__range=(start_date, today))

    products = []
    for order in orders:
        products.extend(order.products.all())

    unique_products = list(set(products))

    context = {
        'ordered_products': unique_products,
        'days': time_period,
    }

    return render(request, 'myapp2/products_ordered_by_customer.html', context)


def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            image = form.cleaned_data['image']
            logger.info(f'Получили {name=}, {description=}, {price=}, {quantity=}.')
            product = Product(name=name, description=description, price=price, quantity=quantity, image=image)
            product.save()
            message = 'Товар сохранён'
    else:
        form = ProductForm()
        message = 'Заполните форму'
    return render(request, 'myapp2/product_form.html', {'form': form, 'message': message})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp2/products.html', {'products': products})


def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'myapp2/update_product.html', {'form': form, 'product': product})


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete_product.html', {'product': product})