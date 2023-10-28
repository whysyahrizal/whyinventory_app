from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from main.models import Item
from main.forms import ItemForm
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import datetime


def register(request) : 
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def create_Item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        Item = form.save(commit=False)
        Item.user = request.user
        Item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def edit_item(request, id):
    item = Item.objects.get(pk = id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_Item(request, id):
    Item = Item.objects.get(pk = id)
    Item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def contact_us(request) :
    return render(request, 'contact_us.html')

@login_required(login_url='/login')
def show_main(request):
    item = Item.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'class': 'PBP A',
        'last_login': request.COOKIES['last_login'],
        'Items': item
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def show_item(request) :
    item = Item.objects.filter(user=request.user)

    context = {
        "items" : item
    }
    return render(request, "show_item.html", context)

@login_required(login_url='/login')
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_item'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login')
def add_item_amount(request,id):
    data = get_object_or_404(Item, pk=id)
    data.amount+=1
    data.save()
    return HttpResponseRedirect(reverse('main:show_item'))

@login_required(login_url='/login')
def delete_item(request,id):
    data = get_object_or_404(Item, pk=id)
    data.delete()
    return HttpResponseRedirect(reverse('main:show_item'))

@login_required(login_url='/login')
def get_item(request):
    items = Item.objects.filter(user=request.user)
    data = [{'id': item.id, 'name': item.name, 'amount': item.amount, 'description': item.description, 'date_added': item.date_added} for item in items]
    return JsonResponse(data, safe=False)

@login_required(login_url='/login')
def create_item_ajax(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})
    else:
        return JsonResponse({'success': False, 'errors': 'Invalid request method'})
