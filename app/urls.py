"""getloop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import SectionListView, SectionDetailView, ItemListView, ItemDetailView, ModifiersListView, ModifiersDetailView

urlpatterns = [
    path('list-section/', SectionListView.as_view(), name='api-section-list'),
    path('section-detail/<pk>/', SectionDetailView.as_view(), name='api-section-detail'),
    path('list-item/', ItemListView.as_view(), name='api-item-list'),
    path('item-detail/<pk>/', ItemDetailView.as_view(), name='api-item-detail'),
    path('list-modifiers/', ModifiersListView.as_view(), name='api-modifiers-list'),
    path('modifiers-detail/<pk>/', ModifiersDetailView.as_view(), name='api-modifiers-detail'),
]
