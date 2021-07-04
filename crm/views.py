from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceTable, PriceCard


# Create your views here.
def first_page(request):
    # object_list = Order.objects.all()
    # form = OrderForm()
    # return render(request, './index.html', {'object_list': object_list,
    #                                        'form': form})

    slider_list = CmsSlider.objects.all()

    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)

    price_table = PriceTable.objects.all()

    form = OrderForm()

    dir_obj = {'slider_list': slider_list,
               'pc_1': pc_1,
               'pc_2': pc_2,
               'pc_3': pc_3,
               'price_table': price_table,
               'form': form,
               }

    return render(request, './index.html', dir_obj)


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name=name, order_phone=phone)
    element.save()
    return render(request, './thanks.html', {'name': name})
