from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('regions/', views.regions_list, name='regions'),
    path('regions/<slug:slug>', views.region, name='region'),
    path('species/<slug:slug>', views.category_species, name='category'),
    path('species/', views.species_list, name='species'),
    path('species/<slug:category_slug>/<slug:specie_slug>', views.specie, name='specie'),
]
