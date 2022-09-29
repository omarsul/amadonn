from django.shortcuts import render,redirect
from .models import Order, Product
from django.db.models import Sum

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(request.POST["price"])
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    
    context= {
        'products': Order.objects.all(),
        'price': total_charge,
        'quantity': quantity_from_form,
        
    }
    return render(request, "store/checkout.html",context)

def check(request):
    
    return redirect("checkout/")