from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', views.home, name='home'),
    path('limited/', views.limited, name='limited_hot_girl_tummy_problems'),
    path('not/', views.not_allowed, name='absolutely_not_hot_girl_tummy_problems'),
    path('free/', views.free, name='hot_girl_tummy_problems'),
]
