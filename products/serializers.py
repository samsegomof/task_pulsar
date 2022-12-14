from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Сериалайзер модели товара"""

    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_image(self, img):
        img_url = img.image.url
        return {
            'path': img_url[:img_url.rindex('.')],
            'formats': [img_url[img_url.rfind('.')+1:], 'webp']
            }
