from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import Product
from .seializers import ProductListSerializer, ProductDetailSerializer


class ProductAPIView(ListAPIView):
    """Product list api view, shows 20 products per page with product's
        name, slug, code, stock status.
        Also the slug field is clickable and leads to it's detail view.
    """
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailAPIView(RetrieveAPIView):
    """Product detail api view, shows product's
        name, slug, code, stocks.
    """
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'


class SizeCreateAPIView(CreateAPIView):
    pass


class ColorCreateAPIView(CreateAPIView):
    pass


class PriceCreateAPIView(CreateAPIView):
    pass
