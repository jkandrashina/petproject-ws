from django.shortcuts import render, get_object_or_404
from .models import Category, Region, Species


def home(request):
    categories = Category.objects.all()
    regions = Region.objects.all()
    return render(request, 'waddensea/home.html', {'categories': categories, 'regions': regions})

def regions_list(request):
    regions = Region.objects.all()
    return render(request, 'waddensea/regions.html', {'regions': regions})

def region(request, slug):
    rgn = get_object_or_404(Region, slug=slug)
    return render(request, 'waddensea/region.html', {'rgn': rgn})

def category_species(request, slug):
    cat = get_object_or_404(Category, slug=slug)
    species_cat = cat.species_set.all()
    return render(request, 'waddensea/category.html', {'species_cat': species_cat, 'cat': cat})

def species_list(request):
    species = Species.objects.all()
    return render(request, 'waddensea/species.html', {'species': species})

def specie(request, category_slug, specie_slug):
    spc = get_object_or_404(Species, slug=specie_slug)
    return render(request, 'waddensea/specie.html', {'spc': spc})
