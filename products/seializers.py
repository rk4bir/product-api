from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Product


class ProductListSerializer(HyperlinkedModelSerializer):
    """Serializer class for Product list view"""
    # detail view is click-able field that leads to product-detail view
    detail_view = serializers.HyperlinkedIdentityField(view_name='product-detail',
                                                       lookup_field='slug',
                                                       lookup_url_kwarg='slug',
                                                       format='html')

    class Meta:
        model = Product
        fields = ['detail_view', 'slug', 'pid', 'title', 'stock_status']


class ProductDetailSerializer(ModelSerializer):
    """Serializer class for product detail view"""

    class Meta:
        model = Product
        # names, product code, slug, status, stocks
        fields = ['title', 'pid', 'slug', 'stocks']
