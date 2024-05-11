"""
URL configuration for ECOMERCEPROJECT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Your existing URL patterns
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = [
   
    path('',views.login),
    path('register/',views.register),
    path('logout/',views.logout,name='logout'),
    path('homepage/',views.homepage),
    path('otp/verify/',views.otp_verify),
    path('addcart/',views.Addcart),
    path('cart/',views.cart),
    path('remove_product/',views.remove_product),
    path('check_out/',views.check_out),
    path('confirm_order/',views.confirm_order),
 #   path('header/',views.header),
    path('footer/',views.footer),
    path('otp/',views.otp),
    path('cart_count/',views.cart_count),
    path('profile/',views.profile), 
    path('search/',views.search),
    path('order_detail_page/',views.order_detail_page),
    path('category/', views.category , name='category'),
    path('category_type/', views.category_type , name='category_type'),
  #  path('order/<int:order_id>/delete/',views.delete_order, name='delete_order'),
  
    path('shipped_orders/', views.shipped_orders, name='shipped_orders'),
    path('new_orders/', views.new_orders, name='new_orders'),
    path('delivered_orders/', views.delivered_orders, name='delivered_orders'),
    path('cancel_orders/', views.cancel_orders, name='cancel_orders'),
    path('all_orders/', views.all_orders, name='all_orders'),
  #  path('order-status/',views.order_status, name='order_status'),
    # path('youtube/',views.youtube),
    # path('video/',views.video),
    # path('meesho/',views.meesho),
    path('mypayments/',views.mypayments),




 
    
   


    path('productdt/<str:product_id>/',views.productdt,name= 'productdt'),


]
