from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from mptt.admin import MPTTModelAdmin

from .models import *


# class CategoryAdmin(DjangoMpttAdmin):
#     prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(DjangoMpttAdmin):
    """
    Админ-панель модели категорий
    """
    list_display = ('id', 'title', 'slug')
    list_display_links = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(ProductColor)
admin.site.register(ProductSize)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.register(ProductGroup)
