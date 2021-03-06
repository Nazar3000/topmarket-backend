from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters
from .models import Product, Category


User = get_user_model()

class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    category_id = filters.ModelChoiceFilter(
        field_name='category',
        queryset=Category.objects.all()
    )
    in_stock = filters.BooleanFilter(
        method='filter_in_stock'
    )
    brand = filters.CharFilter(field_name='brand', lookup_expr='icontains')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    vendor_code = filters.CharFilter(field_name='vendor_code', lookup_expr='icontains')
    user_id = filters.ModelChoiceFilter(
        field_name='user',
        queryset=User.objects.filter(role='CONTRACTOR')
    )

    class Meta:
        model = Product
        fields = [
            'category_id',
            'name',
            'vendor_code',
            'min_price',
            'max_price',
            'in_stock',
            'user_id'
        ]

    def filter_in_stock(self, queryset, name, value):
        if value:
            return queryset.filter(count__gte=1)
        if not value:
            return queryset.filter(count=0)
        return queryset
