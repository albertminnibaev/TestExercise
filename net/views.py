from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from net.filters import NetFilter
from net.models import Net, Product
from net.serializers import NetSerializer, ProductSerializer


class NetViewSet(viewsets.ModelViewSet):
    queryset = Net.objects.all()
    serializer_class = NetSerializer
    filter_backends = [DjangoFilterBackend] # Подключаем библотеку, отвечающую за фильтрацию к CBV
    filterset_class = NetFilter


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

