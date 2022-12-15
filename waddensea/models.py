from django.db import models
from django.urls import reverse
from datetime import date


def base_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/category/<filename>
    return 'images/{0}/{1}'.format(instance.category.slug, filename)

def entity_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/entity_name/<filename>
    return 'images/{0}/{1}'.format(instance.slug, filename)


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    image = models.ImageField(
        upload_to=entity_image_path
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name='URL'
    )
    
    def __str__(self):
        return self.name

    def get_absolute_url(self): 
        return reverse('category', kwargs = {'slug': self.slug})


class Region(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Регион'
    )
    short_desc = models.TextField(
        'Краткое описание'
    )
    desc = models.TextField(
        'Полное описание'
    )
    image = models.ImageField(
        upload_to=entity_image_path
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name='URL'
    )
    
    def __str__(self):
        return self.name

    def get_absolute_url(self): 
        return reverse('region', kwargs = {'slug': self.slug})


class Species(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Название'
    )
    latin_name = models.CharField(
        max_length=150,
        verbose_name='Латинское название'
    )
    short_desc = models.TextField(
        'Краткое описание'
    )
    desc = models.TextField(
        'Полное описание'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )
    region = models.ManyToManyField(
        Region,
        blank=True,
        verbose_name='Регион'
    )
    image = models.ImageField(
        upload_to=base_image_path
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name='URL'
    )
    publication_date = models.DateField(
        default=date.today,
        verbose_name='Дата'
    )
    
    def __str__(self):
        return self.name

    def get_absolute_url(self): 
        return reverse('specie', kwargs = {'category_slug': self.category.slug, 'specie_slug': self.slug})
