from django.urls import path
from . import views
from .views import home
from .views import all_items

urlpatterns = [
    path('', views.home, name='home'),
    path('all/', all_items, name='all_items'),
    path('limited/', views.limited, name='limited_hot_girl_tummy_problems'),
    path('not/', views.not_allowed, name='absolutely_not_hot_girl_tummy_problems'),
    path('free/', views.free, name='hot_girl_tummy_problems'),
    path('log/', views.log, name='log'),
]
