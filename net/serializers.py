from rest_framework import serializers

from net.models import Net, Product
from net.validators import NetValidator


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class NetSerializer(serializers.ModelSerializer):
    product = ProductSerializer(source='product_set', many=True, read_only=True)

    class Meta:
        model = Net
        fields = ['id', 'title', 'email', 'country', 'city', 'treet', 'house', 'net', 'debt', 'created_at',
                  'type', 'level', 'product']
        read_only_fields = ['debt']
        validators = [
            NetValidator(field=('net', 'type'))
        ]
