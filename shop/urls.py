from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.ProductListAPIView.as_view(), name='product_list'),
    path('<slug:category_slug>/', views.ProductListAPIView.as_view(), name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.ProductDetailAPIView.as_view(), name='product_detail'),
]
