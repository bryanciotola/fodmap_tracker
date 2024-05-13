from django.core.serializers import serialize
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import FoodItem

def home(request):
    return render(request, 'diet_manager/home.html')

def limited(request):
    items = FoodItem.objects.filter(category='LIMIT')
    items_json = serialize('json', items, fields=('name', 'details'))  # Specifying fields for clarity
    paginator = Paginator(items, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'diet_manager/category.html', {
        'items_json': items_json,
        'page_obj': page_obj,
        'title': 'Limited Hot Girl Tummy Problems'
    })

def not_allowed(request):
    items = FoodItem.objects.filter(category='FREE')
    items_json = serialize('json', items, fields=('name', 'details'))  # Specifying fields for clarity
    paginator = Paginator(items, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'diet_manager/category.html', {
        'items_json': items_json,
        'page_obj': page_obj,
        'title': 'Absolutely Not Hot Girl Tummy Problems'
    })

def free(request):
    items = FoodItem.objects.filter(category='NO')
    items_json = serialize('json', items, fields=('name', 'details'))  # Specifying fields for clarity
    paginator = Paginator(items, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'diet_manager/category.html', {
        'items_json': items_json,
        'page_obj': page_obj,
        'title': 'Absolutely Not Hot Girl Tummy Problems'
    })


'''
def not_allowed(request):
    item_list = FoodItem.objects.filter(category='NO')
    paginator = Paginator(item_list, 20)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'diet_manager/category.html', {'page_obj': page_obj, 'title': 'Absolutely Not Hot Girl Tummy Problems'})

def free(request):
    item_list = FoodItem.objects.filter(category='FREE')
    paginator = Paginator(item_list, 20)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'diet_manager/category.html', {'page_obj': page_obj, 'title': 'Hot Girl Tummy Problems'})
'''