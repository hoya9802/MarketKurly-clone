from collections.abc import Sequence
from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from .models import Products, Category

# Create your views here.
class ProductLV(ListView):
    model = Products
    context_object_name = "product_list"

class ProductDV(DetailView):
    model = Products

class NewProductLV(ListView):
    model = Products
    template_name = 'product/new_list.html'
    ordering = ('-create_dt')

    paginate_by= 6

class MainCategoryLV(ListView):
    model = Products
    template_name = 'product/main_category_list.html'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        subcategories = Category.objects.filter(parent_category_id=category_id)
        return Products.objects.filter(category__in=subcategories)
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = Category.objects.get(id=category_id)
        context['category'] = category
        context['subcategory'] = category.subcategory.all()
        return context
        

class SubCategoryLV(ListView):
    model = Products
    template_name = 'product/sub_category_list.html'
    paginate_by = 3

    def get_queryset(self) -> QuerySet[Any]:
        subcategory_id = self.kwargs.get('subcategory_id')
        return Products.objects.filter(category_id=subcategory_id)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        subcategory_id = self.kwargs.get('subcategory_id')
        subcategory = Category.objects.get(id=subcategory_id)
        
        context['subcategory'] = subcategory
        return context
