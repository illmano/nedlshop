# Generated by Django 4.1.7 on 2023-03-27 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_category_options_rename_name_category_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='products', to='catalog.category', verbose_name='Выберите катeгорию'),
        ),
    ]
