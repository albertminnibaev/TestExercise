from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from net.filters import NetFilter
from net.models import Net, Product
from net.permissions import IsActiv
from net.serializers import NetSerializer, ProductSerializer


class NetViewSet(viewsets.ModelViewSet):
    queryset = Net.objects.all()
    serializer_class = NetSerializer
    filter_backends = [DjangoFilterBackend]  # Подключаем библотеку, отвечающую за фильтрацию к CBV
    filterset_class = NetFilter
    # permission_classes = IsActiv

    def perform_create(self, serializer):
        new_net = serializer.save()
        if new_net.type == "Индивидуальный предприниматель":
            new_net.level = 1
        if new_net.type == "Розничная сеть":
            if new_net.net.type == "Завод":
                new_net.level = 1
            else:
                new_net.level = 2
        new_net.save()

    def get_permissions(self):
        return [(IsAuthenticated | IsActiv)()]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsActiv]

    def get_permissions(self):
        return [(IsAuthenticated | IsActiv)()]
