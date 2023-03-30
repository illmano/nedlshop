from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse

from utils import upload_function


class Category(MPTTModel):
    """Сategories to which the goods belong"""
    title = models.CharField(max_length=150, db_index=True, verbose_name="Название категорий")
    slug = models.SlugField(max_length=200, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Родительская категория'
    )

    class MPTTMeta:
        order_insertion_by = ('title',)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class ProductGroup(models.Model):
    """Группа продуктов"""
    name = models.CharField(max_length=255, verbose_name='Группа товаров')
    slug = models.SlugField(max_length=250)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Группа товаров'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Product(models.Model):
    """Model of product"""
    category = models.ManyToManyField(Category, related_name="products", verbose_name='Выберите катeгорию')
    group = models.ForeignKey(
        ProductGroup, null=False, blank=False, verbose_name='Группа товаров', on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=250, db_index=True)
    article = models.CharField(max_length=20, verbose_name='Артикул')
    color = models.ForeignKey('ProductColor', null=False, blank=False, on_delete=models.CASCADE, verbose_name='Цвет')
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True, verbose_name='Фото товара')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Доступно')
    quantity = models.IntegerField(verbose_name='Наличие на складе')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


class ProductColor(models.Model):
    """Цвет продукта"""
    name = models.CharField(max_length=30, verbose_name="Название цвета")

    class Meta:
        ordering = ('name',)
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    """Размер продукта"""
    name = models.CharField(max_length=10, verbose_name="Размер")

    class Meta:
        ordering = ('name',)
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.name
