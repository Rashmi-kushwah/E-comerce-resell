from django.db import models

# Create your models here.

import uuid

class Productdt(models.Model):
    Product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)  # Name ya title of the top
    price = models.DecimalField(max_digits=20, decimal_places=2)  # Price ya daam
    sku_code = models.CharField(max_length=30, blank=True, null=True)
    title= models.CharField(max_length=60, blank=True, null=True)
    mrp = models.IntegerField()
    sub_title = models.CharField(max_length=60, blank=True, null=True)
    brand = models.CharField(max_length=100)  # Brand ka naam
    color = models.CharField(max_length=50)  # Rang
    Category = models.CharField(max_length=20, blank=True, null=True)
    material = models.CharField(max_length=100)  # Material (cotton, silk, etc.)
    sleeve_length = models.CharField(max_length=50)  # Sleeve length (full, half, etc.)
    neckline = models.CharField(max_length=50)  # Neckline style (round, V-neck, etc.)
    pattern = models.CharField(max_length=100)  # Pattern (solid, floral, etc.)
    occasion = models.CharField(max_length=100)  # Occasion (casual, party wear, etc.)
    Model_name = models.CharField(max_length=20, blank=True, null=True)
    
    # Image fields
    img1 = models.CharField(max_length=200, blank=True, null=True)
    img2 = models.CharField(max_length=200, blank=True, null=True)
    img3 = models.CharField(max_length=200, blank=True, null=True)
    img4 = models.CharField(max_length=200, blank=True, null=True)
    img5 = models.CharField(max_length=200, blank=True, null=True)
    img6 = models.CharField(max_length=200, blank=True, null=True)
    img7 = models.CharField(max_length=200, blank=True, null=True)
    img8 = models.CharField(max_length=200, blank=True, null=True)
    
    size1 = models.CharField(max_length=50, blank=True, null=True)#small, medium,large
    size2 = models.CharField(max_length=50, blank=True, null=True)
    size3 = models.CharField(max_length=50, blank=True, null=True)

    qty1 = models.IntegerField()
    qty2 = models.IntegerField()
    qty3 = models.IntegerField()
    qty4 = models.IntegerField()

    net_quantity = models.IntegerField() 
    description = models.CharField(max_length=30, blank=True, null=True)
    
    def __str__(self):
        return self.name



from django.contrib import admin

# Register your models here.
from .models import Productdt
# Register your models here.

    
@admin.register(Productdt)
class ProductAdmin(admin.ModelAdmin):
   
    list_display = [field.name for field in  Productdt._meta.fields]   
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        category = request.GET.get('Category')  # 'Category' ko 'category' me change kiya gaya
        if category:
            queryset = queryset.filter(Category=category)
        return queryset