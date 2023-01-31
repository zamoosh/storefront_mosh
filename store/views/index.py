from .imports import *


def index(request):
    # products = Product.objects.all().select_related('collection')
    orders = Order.objects.order_by('-placed_at').select_related('customer').prefetch_related('orderitem_set__product')[:5]
    order_count = Customer.objects.filter(id=1)[0].order_set.all()[0].orderitem_set.count()
    order_count = Customer.objects.filter(id=1)[0].order_set.all().prefetch_related('orderitem_set').aggregate(Count('orderitem_set__id'))
    print(order_count)
    return render(request, f'{__name__.replace(".", "/")}.html', {'orders': orders})
