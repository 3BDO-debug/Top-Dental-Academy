from django.shortcuts import render, redirect, HttpResponse
from .models import Order
from Course.models import Course
from django.contrib import messages
# Create your views here.

def create_order(request, id):
    if request.user.is_authenticated:
        Order.objects.create(order_owner=request.user, ordered_course=Course.objects.get(id=id)).save()
        return HttpResponse('Order Had been Placed')
    else:
        messages.info(request, "You Have To login first to Buy Course")
        return redirect('/Accounts/Run/login')