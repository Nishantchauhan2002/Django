from django.urls import path
from . import views

urlpatterns = [
    path('', views.allItems,name = "all_items"),
]
