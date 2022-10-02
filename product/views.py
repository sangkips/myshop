from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, get_user_model, login, logout
from product.forms import ProductForm, UserRegisterForm
from product.models import Product


def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product/index.html', context)


def registerUserView(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'product/register.html', context)



@login_required(login_url='login')
def createProductView(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'product/create.html', context)


@login_required(login_url='login')
def updateProductView(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'product/update.html', context)


@login_required(login_url='login')
def deleteProductView(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    context = {
        'product': product
    }
    return render(request, 'product/delete.html', context)


def addToCart(request):
    context = {}
    return render(request, 'product/addtocart.html', context)


def removeFromCart(request):
    context = {}
    return render(request, 'product/removefromcart.html', context)
