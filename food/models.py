from django.db import models
from django.urls import reverse
from django.contrib.auth.models import Permission, User
from django.conf import settings
from django.db.models.signals import pre_save
from .utils import unique_slug_generator

User=settings.AUTH_USER_MODEL



class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    nick_names = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150,blank=True, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   # class Meta:
   #     ordering = ('name', )
    #    verbose_name = 'category'
   #     verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

  #  def get_absolute_url(self):
  #      return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category  , on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    nick_names = models.CharField(max_length=400, db_index=True)
    slug = models.SlugField(max_length=150,blank=True, unique=True ,db_index=True)
    description = models.TextField(blank=True)
    b_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.CharField(max_length=15, db_index=True)

    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    logo=models.FileField()

    #class Meta:
      #  ordering = ('name', )
     #   index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

#    def get_absolute_url(self):
    #    return reverse('shop:product_detail', args=[self.id, self.slug])



def category_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug= unique_slug_generator(instance)

pre_save.connect(category_pre_save_receiver,sender=Category)

def product_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug= unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver,sender=Product)

