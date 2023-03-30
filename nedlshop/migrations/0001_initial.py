# Generated by Django 4.1.7 on 2023-03-26 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_products', models.IntegerField(default=0, verbose_name='Общее количество товаров')),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая стоимость')),
                ('in_order', models.BooleanField(default=False)),
                ('for_anonymous_user', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Крозины',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Название категорий')),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активность')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Покупатель',
                'verbose_name_plural': 'Покупатели',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='product/%Y/%m/%d', verbose_name='Фото товара')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Цена')),
                ('available', models.BooleanField(default=True, verbose_name='Доступно')),
                ('quantity', models.IntegerField(verbose_name='Наличие на складе')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='nedlshop.category', verbose_name='Выберите катeгорию')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('address', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Адрес')),
                ('status', models.CharField(choices=[('new', 'Новый заказ'), ('in_progress', 'Заказ в обработке'), ('is_ready', 'Заказ готов'), ('completed', 'Заказ получен')], default='new', max_length=100, verbose_name='Статус заказа')),
                ('buying_type', models.CharField(choices=[('self', 'Самовывоз'), ('delivery', 'Доставка')], max_length=100, verbose_name='Тип доставки')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к заказу')),
                ('created_at', models.DateField(auto_now=True, verbose_name='Дата создания заказа')),
                ('order_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата доставки')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nedlshop.cart', verbose_name='Корзина')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='nedlshop.customer', verbose_name='Покупатель')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_orders',
            field=models.ManyToManyField(blank=True, related_name='related_customer', to='nedlshop.order', verbose_name='Заказы пользователя'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='customer',
            name='wishlist',
            field=models.ManyToManyField(blank=True, to='nedlshop.product', verbose_name='Список желаемого'),
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая цена')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nedlshop.cart', verbose_name='Корзина')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nedlshop.customer', verbose_name='Покупатель')),
            ],
            options={
                'verbose_name': 'Продукт корзины',
                'verbose_name_plural': 'Продукты корзины',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nedlshop.customer', verbose_name='Покупатель'),
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, related_name='related_cart', to='nedlshop.cartproduct', verbose_name='Продукты для корзины'),
        ),
    ]
