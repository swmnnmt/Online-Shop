from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from shop.models import Category, Product
from rest_framework.renderers import TemplateHTMLRenderer


class ProductListAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/product/list.html'

    def get(self, request, category_slug=None):
        category = None
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        return Response({'category': category,
                         'categories': categories,
                         'products': products})


class ProductDetailAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/product/detail.html'

    def get(self, request, id, slug):
        product = get_object_or_404(Product,
                                    id=id,
                                    slug=slug,
                                    available=True)
        return Response({'product':product})
