from rest_framework import serializers

from net.models import Net, Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class NetSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Net
        fields = "__all__"# ['title', 'email', 'country', 'city', 'treet', 'house', 'net', 'debt', 'created_at', 'product']
        read_only_fields = ['debt']
