from django.urls import path

from .views import images, category_api, product_api, search_api, related_product_api, filter_api,\
    ordered_products, checkout

urlpatterns = [
    path('categories/', category_api),
    path('products/', product_api),
    path('product/', search_api),
    path('filter/', filter_api),
    path('ordered-products/', ordered_products),
    path('checkout/', checkout),
    path('related-products/<int:pk>', related_product_api),

]