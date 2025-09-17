from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from .models import Supplier, Product, Transaction


# Existing registrations
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "contact", "address")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "stock", "supplier")


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "transaction_type", "quantity", "date")


# Custom Dashboard
class CustomAdminSite(admin.AdminSite):
    site_header = "Mini ERP Dashboard"
    site_title = "Mini ERP Admin"
    index_title = "Welcome to Mini ERP"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("dashboard/", self.admin_view(self.dashboard_view), name="dashboard"),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        total_products = Product.objects.count()
        low_stock_products = Product.objects.filter(stock__lt=10)
        total_inventory_value = sum(p.price * p.stock for p in Product.objects.all())

        context = dict(
            self.each_context(request),
            total_products=total_products,
            low_stock_products=low_stock_products,
            total_inventory_value=total_inventory_value,
        )
        return TemplateResponse(request, "admin/dashboard.html", context)


# Replace default admin site with custom one
custom_admin_site = CustomAdminSite(name="custom_admin")
custom_admin_site.register(Supplier, SupplierAdmin)
custom_admin_site.register(Product, ProductAdmin)
custom_admin_site.register(Transaction, TransactionAdmin)
