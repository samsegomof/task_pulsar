# Generated by Django 4.1.4 on 2022-12-13 23:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('article', models.PositiveIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1, message='Артикул должен быть не менее 1')], verbose_name='Артикул товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('status', models.CharField(choices=[('ВН', 'В наличии'), ('ПЗ', 'Под заказ'), ('ОП', 'Ожидает поступления'), ('НН', 'Нет в наличии'), ('НП', 'Не производится')], default='ВН', max_length=2, verbose_name='Статус')),
                ('image', models.ImageField(upload_to='media/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ('status',),
            },
        ),
    ]
