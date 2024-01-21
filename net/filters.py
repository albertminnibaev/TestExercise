import django_filters
from django_filters import rest_framework

from net.models import Net


class NetFilter(django_filters.rest_framework.FilterSet):
    country = rest_framework.CharFilter(field_name='country', lookup_expr='icontains')

    class Meta:
        model = Net
        fields = ('country',)
