from django.urls import path

from .views import  category_api, product_detail, product_api, search_api, related_product_api, filter_api,\
    ordered_products, checkout, filter_by_child_api, filter_by_parent_api, child_categories, sub_categories, featured_products, best_products

urlpatterns = [
    path('categories/', category_api),
    path('child-categories/<int:pk>/', child_categories),
    path('sub-categories/<int:pk>/', sub_categories),
    path('products/', product_api),
    path('product/', search_api),
    path('filter-by-parent/', filter_by_parent_api),
    path('filter-by-child/', filter_by_child_api),
    path('filter/', filter_api),
    path('product-detail/<int:pk>/', product_detail),
    path('ordered-products/<int:pk>/', ordered_products),
    path('checkout/', checkout),
    path('featured-products/', featured_products),
    path('bestseller-products/', best_products),
    path('related-products/<int:pk>', related_product_api),

]