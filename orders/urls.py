from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^order_created/$', views.order_created, name='order_created'),

    url(r'^your_order/$', views.your_order, name='your_order'),
]