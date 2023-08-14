from django.shortcuts import render, get_object_or_404
from category.models import Category
from .models import Product

def showcategories(request):
    cat=Category.objects.all()
    return render(request,"shop.html",{'c':cat})


def showproducts(request, category=None):
    if category:
        categories = get_object_or_404(Category, slug=category)
        product1 = Product.objects.all()
        product = product1.filter(category=categories)
        return render(request, 'Product_details.html', {'product': product})


def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Login & Try Again")
        return redirect('/login')
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amt')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        Order = Orders(items_json=items_json, name=name, amount=amount, email=email, address1=address1,
                       address2=address2, city=city, state=state, zip_code=zip_code, phone=phone)
        print(amount)
        Order.save()
        update = OrderUpdate(order_id=Order.order_id, update_desc="the order has been placed")
        update.save()
        thank = True
        id = Order.order_id
        oid = str(id)
        oid = str(id)
        param_dict = {

            'MID': 'add ur merchant id',
            'ORDER_ID': oid,
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'paytm.html', {'param_dict': param_dict})

    return render(request, 'checkout.html')




