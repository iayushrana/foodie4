from django.db import models
from food.models import Product
from django.contrib.auth.models import Permission, User


class Order(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    phone_no = models.IntegerField()
    address = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    total_cost=models.DecimalField(max_digits=15, default=22,decimal_places=2)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    total_i_price=models.DecimalField(max_digits=15, decimal_places=2)


    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

