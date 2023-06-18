from django.shortcuts import render

# Create your views here.
def cart(requsets):
    return render(requsets,'cart.html',name=cart)
def order_history(request):
    return render(request,'order history.html',name='order_histort')