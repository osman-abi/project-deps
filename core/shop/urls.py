from django.urls import path

from .views import  category_api, product_detail, product_api, search_api, related_product_api, filter_api,\
    ordered_products, checkout

urlpatterns = [
    path('categories/', category_api),
    path('products/', product_api),
    path('product/', search_api),
    path('filter/', filter_api),
    path('product-detail/<int:pk>/', product_detail),
    path('ordered-products/', ordered_products),
    path('checkout/', checkout),
    path('related-products/<int:pk>', related_product_api),

]