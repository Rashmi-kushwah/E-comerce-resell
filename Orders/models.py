from django.db import models

# Create your models here.
from django.db import models

class Order(models.Model):
    Product_id = models.CharField(max_length=50, null=True, blank=True)
    user_uid = models.CharField(max_length=50,null=True, blank=True)
    name = models.CharField(max_length=100 ,null=True, blank=True)  # Name of the customer
    email = models.EmailField()  # Corresponds to the Email field in the form
    phone_number = models.CharField(max_length=10,null=True, blank=True)  # Mobile number of the customer
    address = models.TextField(null=True, blank=True)  # Address of the customer
    landmark = models.CharField(max_length=100,null=True, blank=True)  # Landmark near the address
    pincode = models.CharField(max_length=10,null=True, blank=True)  # Pincode of the customer's area
    state = models.CharField(max_length=100,null=True, blank=True)  # State name
    country = models.CharField(max_length=50,null=True, blank=True)  # Corresponds to the Country field in the form
    payment_method = models.CharField(max_length=50,null=True, blank=True) 
    order_id =models.CharField(max_length=100,null=True, blank=True)  # State name
    order_date=models.CharField(max_length=100,null=True, blank=True)  # State name
    tracking_id=models.CharField(max_length=100,null=True, blank=True)  # State name
    tracking_link=models.CharField(max_length=100,null=True, blank=True)  # State name
    order_status=models.CharField(max_length=100,null=True, blank=True)  # State name
    reselling_amount= models.CharField(max_length=30,null=True, blank=True)
    resell_margin = models.CharField(max_length=30,null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2,null=True, blank=True)
    total_qty = models.CharField(max_length=30,null=True, blank=True)
    img1 = models.CharField(max_length=200, blank=True, null=True)

   

    

   
