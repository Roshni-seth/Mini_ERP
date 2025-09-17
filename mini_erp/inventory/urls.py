from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('products/', views.products_page, name="products"),
    path('suppliers/', views.suppliers_page, name="suppliers"),
    path('transactions/', views.transactions_page, name="transactions"),
]
