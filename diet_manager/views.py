from django.core.serializers import serialize
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import FoodItem

def home(request):
    return render(request, 'diet_manager/home.html')

def all_items(request):
    items = FoodItem.objects.all()  # Get all items
    return render(request, 'diet_manager/all_items.html', {'items': items, 'title': 'all the food !'})



def limited(request):
    items = FoodItem.objects.filter(category='LIMIT')
    items_json = serialize('json', items, fields=('name', 'details'))  # Specifying fields for clarity
    paginator = Paginator(items, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'diet_manager/category.html', {
        'items_json': items_json,
        'page_obj': page_obj,
        'title': 'limits !'
    })

def not_allowed(request):
    items = FoodItem.objects.filter(category='NO')
    items_json = serialize('json', items, fields=('name', 'details'))  # Specifying fields for clarity
    paginator = Paginator(items, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'diet_manager/category.html', {
        'items_json': items_json,
        'page_obj': page_obj,
        'title': 'absolutely not !'
    })

def free(request):
    items = FoodItem.objects.filter(category='FREE')
    items_json = serialize('json', items, fields=('name', 'details'))  # Specifying fields for clarity
    paginator = Paginator(items, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'diet_manager/category.html', {
        'items_json': items_json,
        'page_obj': page_obj,
        'title': 'hot girl tummy problems'
    })

def log(request):
    return render(request, 'diet_manager/log.html')  # Ensure you have a log.html template

