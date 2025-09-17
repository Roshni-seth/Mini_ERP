from django.shortcuts import render, redirect
from .models import Product, Supplier, Transaction

def dashboard(request):
    total_products = Product.objects.count()
    low_stock = Product.objects.filter(stock__lt=10)
    total_value = sum(p.price * p.stock for p in Product.objects.all())

    return render(request, "dashboard.html", {
        "total_products": total_products,
        "low_stock": low_stock,
        "total_value": total_value
    })


def products_page(request):
    if request.method == "POST":
        name = request.POST["name"]
        price = request.POST["price"]
        stock = request.POST["stock"]
        supplier_id = request.POST["supplier"]
        supplier = Supplier.objects.get(id=supplier_id)
        Product.objects.create(name=name, price=price, stock=stock, supplier=supplier)
        return redirect("/products/")

    products = Product.objects.all()
    suppliers = Supplier.objects.all()
    return render(request, "products.html", {"products": products, "suppliers": suppliers})


def suppliers_page(request):
    if request.method == "POST":
        Supplier.objects.create(
            name=request.POST["name"],
            contact=request.POST.get("contact", ""),
            address=request.POST.get("address", "")
        )
        return redirect("/suppliers/")

    suppliers = Supplier.objects.all()
    return render(request, "suppliers.html", {"suppliers": suppliers})


def transactions_page(request):
    if request.method == "POST":
        product = Product.objects.get(id=request.POST["product"])
        t_type = request.POST["transaction_type"]
        qty = int(request.POST["quantity"])
        Transaction.objects.create(product=product, transaction_type=t_type, quantity=qty)
        return redirect("/transactions/")

    transactions = Transaction.objects.all().order_by("-date")
    products = Product.objects.all()
    return render(request, "transactions.html", {"transactions": transactions, "products": products})
