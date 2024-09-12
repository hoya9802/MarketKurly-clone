from django.urls import path
from .views import ProductLV, ProductDV, NewProductLV, MainCategoryLV, SubCategoryLV, SearchProductLV

app_name = 'product'

urlpatterns = [
    path('', ProductLV.as_view(), name='index'),
    path('detail/<int:pk>/', ProductDV.as_view(), name='product_detail'),
    path('new/', NewProductLV.as_view(), name='new_product'),
    path('category/<int:category_id>/', MainCategoryLV.as_view(), name='main_category'),
    path('subcategory/<int:subcategory_id>/', SubCategoryLV.as_view(), name='sub_category'),
    path('search/', SearchProductLV.as_view(), name='search_products'),
] 