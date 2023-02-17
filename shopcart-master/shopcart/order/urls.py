from django.urls import path
from .views import order_create

app_name = "order"

urlpatterns = [
    path("create/", order_create, name='create')
]