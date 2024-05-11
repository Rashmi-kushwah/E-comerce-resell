from django.contrib import admin

# Register your models here.
from ecomUser.models import User
# Register your models here.

@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
   
    list_display = [field.name for field in User._meta.fields] 
