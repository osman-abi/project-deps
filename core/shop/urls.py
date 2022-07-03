from django.urls import path

from .views import ImagesAPIView, category_api, product_api, search_api, related_product_api, filter_api

urlpatterns = [
    path('categories/', category_api),
    path('products/', product_api),
    path('product/', search_api),
    path('filter/', filter_api),
    path('related-products/<int:pk>', related_product_api),
    path('images/>', ImagesAPIView.as_view()),

]