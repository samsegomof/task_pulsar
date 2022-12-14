from django.db import models
from django.core.validators import MinValueValidator

from products.image_converter import WEBPImage
from pulsar.settings import MEDIA_ROOT


def get_image_path(instance, filename):
    """Путь сохранения изображения"""
    return f'{MEDIA_ROOT}/images/{instance.article}/{filename}'


class Product(models.Model):
    # CHOICES - статусы товаров
    CHOICES = (
        ('ВН', 'В наличии'),
        ('ПЗ', 'Под заказ'),
        ('ОП', 'Ожидает поступления'),
        ('НН', 'Нет в наличии'),
        ('НП', 'Не производится'),
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('status',)

    name = models.CharField(max_length=250, verbose_name='Название')
    article = models.PositiveIntegerField(
        validators=[MinValueValidator(1, message='Артикул должен быть не менее 1')],
        unique=True,
        verbose_name='Артикул товара'
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    status = models.CharField(
        max_length=2,
        choices=CHOICES,
        default='ВН',
        verbose_name='Статус'
    )
    image = WEBPImage(upload_to=get_image_path, verbose_name='Изображения')

    objects = models.Manager()

    def __str__(self):
        return self.name

