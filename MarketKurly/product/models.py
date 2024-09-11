from django.db import models
from django.urls import reverse
from .fields import ThumbImageField

class Category(models.Model):
    name = models.CharField('Category name', max_length=255)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='subcategory') 

    def __str__(self):
        name_parts = [
            'sub:' + self.name if self.parent_category else self.name,
            'main:' + self.parent_category.name if self.parent_category else ''
        ]
        result = (
            " > ".join(
                map(
                    str.strip, 
                    [name_parts[0], name_parts[1]]
                )
            ) if self.parent_category else "{}".format(self.name)
        )
        return result if result and len(result) > 0 else "No Name"


class Products(models.Model):
    image = ThumbImageField(upload_to='product/%Y/%m')
    name = models.CharField('Product name', max_length=255, blank=False, null=False)
    description = models.TextField('Product Description', blank=True)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    create_dt = models.DateField(auto_now_add=True)
    update_dt = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.CharField(max_length=100, default='Kurly')

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product:product_detail', args=(self.id,))