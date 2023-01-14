from .imports import *


def index(request):
    products = Product.objects.all().filter(id__range=(1, 4))
    orders = Order.objects.filter(customer_id=1)
    return render(request, f'{__name__.replace(".", "/")}.html', {'products': products, 'orders': orders})
