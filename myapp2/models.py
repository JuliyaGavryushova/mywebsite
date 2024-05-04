from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    date_registration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Client: {self.name}, phone number: {self.phone_number}, email: {self.email}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_addition = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products', default=None, null=True, blank=True)

    def __str__(self):
        return f'Product: {self.name}, price: {self.price}, quantity: {self.quantity}'


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order: {self.customer}, total price: {self.total_price}'