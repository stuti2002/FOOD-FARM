
from django.http.response import HttpResponse
from django.shortcuts import render ,redirect
from datetime import datetime
from home.models import Contact, Order
from home.forms import NewOrder

# Create your views here.
def home(request):
    return render(request,'index.html')
def menu(request):

    return render(request,"menu.html")

def snacks(request):
    return render(request,'snacks.html')

def lunch(request):
    return render(request,'lunch.html')

def juice(request):
    return render(request,'juice.html')

def desserts(request):
    return render(request,'desserts.html')

def order(request):
    order= NewOrder()
    if request.method=='POST':
        order=NewOrder(request.POST)
        if NewOrder.is_valid(order):
            NewOrder.save(order)
            return redirect('menu')

    context={'order':order}
    return render(request ,'Order_page.html',context)

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
    return render(request,'contact.html')