from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from  ecomUser.models import User
from PRODUCTDT.models import Productdt
from CARTPRODUCT.models import addcart
from Orders.models import Order
from django.contrib.auth import logout
from django.core.paginator import Paginator


<<<<<<< HEAD
from datetime import datetime
import uuid

from django.shortcuts import render
from django.http import HttpResponseRedirect
from Orders.models import Order
import uuid
from datetime import datetime
from django.shortcuts import render, redirect
#from .models import Order  # Import your Order model

=======

>>>>>>> e9aee8372386e4c0b29cea0ce6721898513a1586
'''
def header(request):
    return render(request,"header.html")  
'''

###################################### LOGIN  METHOD START ###############################################
   
def login(request):
    

    if 'message' in request.GET:
        msg= request.GET['message']

    else:
        msg=None
        

    if request.method == 'POST':
        
        email = request.POST.get('email')
        print(email)
        
        password = request.POST.get('password')
        print(password)
        try:
            user = User.objects.get(email=email)
            if password == user.password:  
                request.session['user_uid'] = str(user.user_uid)
                print('check')
                return redirect('/reseller/homepage/')

            else:
                print('no check')
                return render(request, 'login.html', {'error': 'Invalid email or password'})    
      
        except User.DoesNotExist:

            return render(request, 'login.html',{'error': 'Email id is not registered'})
    else:
        return render(request, 'reseller/login.html',{'error':msg})

###################################### LOGIN  METHOD CLOSE #################################################

###################################### REGISTER   METHOD START #################################################
def register(request):   
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number  = request.POST.get('mo')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        
        try:
            user = User.objects.get(email = email)
            return render(request, 'register.html', {'error': 'Email address already registered.'})
        
        except :
            otp = send_otp_email(email)
          #  otp = 1234
            request.session['email'] = email
            # Create user instance
            
            user = User.objects.create(
                Name=name,
                phone_number =phone_number ,
                email=email,
                password=password,
                otp=otp  # Set OTP value in the user instance
            )
            user.save()  # Save the user instance with OTP
         #   return HttpResponse("save")
            return redirect('/reseller/otp/verify/')
    else:
        return render(request, 'reseller/register.html')


###################################### REGISTER  METHOD CLOSE ###############################################

###################################### SEND OTP METHOD START ################################################


from django.core.mail import send_mail
from django.utils.crypto import get_random_string

def send_otp_email(email):
    otp = get_random_string(length=6, allowed_chars='1234567890')
    subject = 'Your OTP for ECOMERCEPROJECT'
    message = f'Your OTP is: {otp}'
    from_email = 'rashmiinfo6@gmail.com'  # Your email ID
    recipient_list = [email]
    
    send_mail(subject, message, from_email, recipient_list)
    print('send email ')
    
    return otp

def otp_verify(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        email = request.session.get('email')
        print(email)
        user = User.objects.get(email=email)
        if otp == user.otp: 
            
            return redirect('/reseller/?message=verification successful') 
        else:
            return render(request,'otp page.html',{'error': 'invalid otp'})    

    return render(request,'reseller/otp page.html')    
        


###################################### SEND OTP METHOD CLOSE ###############################################

######################################  OTP METHOD START ##################################################



def otp(request):
    try:
        user_id = request.session.get('user_uid')
        print('user_id',user_id)
        user = User.objects.get(user_uid=user_id)
        print('user',user)

    except:
     return redirect('/reseller/?message=Please login') 
    return render(request,"otp page.html")


######################################  OTP METHOD CLOSE ###################################################

###################################### LOGOUT METHOD START #################################################   
    

def logout(request):
    try:
            user_id = request.session.get('user_uid')
            print(user_id)
            user = User.objects.get(user_uid=user_id)
            print(user)
         #  user_id = request.session.get('user_uid')
         #   print(user_id)
            if 'user_uid' in request.session:
                del request.session['user_uid']  # Remove user ID from session
        
            return redirect('/reseller/?message=Logged out successfully')
    except:
            return redirect('/reseller/?message=Please login')

###################################### LOGOUT METHOD CLOSE ############################################### 
        
###################################### HOMEPAGE  METHOD  START ###########################################
def homepage(request):
    try:
      
     #   user = User.objects.get(user_uid=user_id)
        user_id = request.session.get('user_uid')
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        print(cart_count )
      
        
        
        all_products = Productdt.objects.all()
        records_per_page = 8
        paginator = Paginator(all_products, records_per_page)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        total_page = page_obj.paginator.num_pages
        data = {
                'products':page_obj,
                'page_obj':page_obj,
                'total_pagelist': [n+1 for n in range(total_page)],
                # 'products': all_products,
                'cart_count': cart_count
            }

        return render(request, 'reseller/homepage.html', data)
    
    except:
       return redirect('/?message=Please login') 
###################################### HOMEPAGE  METHOD  CLOSE ###########################################

###################################### CART COUNT METHOD START ###########################################  
     
def cart_count(request):
    user_id = request.session.get('user_uid')
    cart_product = addcart.objects.filter(user_uid=user_id)
    cart_count = cart_product.count()
    print(cart_count )
    return render(request, 'header.html', {'cart_count': cart_count})


###################################### CART COUNT METHOD CLOSE ##############################################

######################################  PRODUCTDETAIL METHOD START ##########################################  


def productdt(request, product_id):
    try:
        user_id = request.session.get('user_uid')
        print(user_id)
        user = User.objects.get(user_uid=user_id)
        print(user)
        
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        print(cart_count )
  
        # Product detail retrieve karne ke liye product_id ka use karein
        get_product_dt = Productdt.objects.filter(Product_id=product_id)
        print(get_product_dt)
        all_products = Productdt.objects.none()  
        value = None
        
    
        if get_product_dt.exists():
           
            value = get_product_dt.first().Model_name
        
      
            if value is not None:
               
                all_products = Productdt.objects.filter(Model_name__icontains=value)
            #  print(all_products )
        
        # Pass the retrieved product details to the template
        return render(request, 'reseller/product page.html', {'get_product': get_product_dt, 'products': all_products, 'cart_count': cart_count,})
    except:
       return redirect('/reseller/?message=Please login') 


    
###################################### PRODUCTDETAIL METHOD CLOSE  ################################################

###################################### SEARCH METHOD START ########################################################
def search(request):
    try:
        user_id = request.session.get('user_uid')
        print(user_id)
        user = User.objects.get(user_uid=user_id)
        print(user)
        if request.method == 'POST':
            value = request.POST.get('search')
            print(value)
            all_products = Productdt.objects.filter(name__icontains=value)
            print(all_products)
            cart_product = addcart.objects.filter(user_uid=user_id)
            cart_count = cart_product.count()
            print(cart_count )

        
            data={  'cart_count': cart_count,
                    'products': all_products, 
                    
                    'category': value  # Category ka data context mein add karen
                }  
            return render(request, 'reseller/category_page.html',data)
        
    except:
        return redirect('/reseller/?message=Please login') 

##################################### SEARCH METHOD CLOSE ###################################################  

###################################### CATEGORY METHOD  START ###############################################    
    


def category(request):
        try:
            user_id = request.session.get('user_uid')
            print(user_id)
            user = User.objects.get(user_uid=user_id)
            print(user)
        
            #  if request.method == 'POST':
            value = request.GET.get('category_value')
            all_products = Productdt.objects.filter(name__icontains=value)
            print('data not found',all_products)
            user_id = request.session.get('user_uid')
            cart_product = addcart.objects.filter(user_uid=user_id)
            cart_count = cart_product.count()
            print(cart_count )

        
            data={
                    'products': all_products, 
                    'category': value  ,# Category ka data context mein add karen
                    'cart_count': cart_count,
                }
        
            return render(request, 'reseller/category_page.html',data)

        except:
            return redirect('/reseller/?message=Please login')


###################################### CATEGORY METHOD  CLOSE ###############################################  
        
######################################  CATEGORY TYPE METHOD START  #########################################            

def category_type(request):
        try:
            user_id = request.session.get('user_uid')
            print(user_id)
            user = User.objects.get(user_uid=user_id)
            print(user)
        #  if request.method == 'POST':
            value = request.GET.get('category_value')
            all_products = Productdt.objects.filter(Category__icontains=value)
            print('data not found',all_products)
            user_id = request.session.get('user_uid')
            cart_product = addcart.objects.filter(user_uid=user_id)
            cart_count = cart_product.count()
            print(cart_count )

        
            data={
                    'products': all_products, 
                    'category': value  ,# Category ka data context mein add karen
                    'cart_count': cart_count,
                    'category': value  # Category ka data context mein add karen
                }
        
            return render(request, 'reseller/category_page.html',data)
        except:
            return redirect('/reseller/?message=Please login') 




        
###################################### CATEGORY METHOD  CLOSE ####################################################         
    
###################################### ADDCART METHOD START ####################################################### 



def Addcart(request):
    try:
            user_id = request.session.get('user_uid')
            print(user_id)
            user = User.objects.get(user_uid=user_id)
            print(user)
            if request.method == 'POST':
            
            #  print("Session User ID:", user_id)
                product_id = request.POST.get('product_id')
                print("Add Product ID:", product_id)
                buy_id = request.POST.get('buy_id')
                print("Add buy ID:", buy_id)
                size = request.POST.get('sizes')
                print("Selected Size:", size)
                qty = request.POST.get('qty')
                print("Selected Quantity:", qty)
              
                try:
                    add_product_dt = Productdt.objects.get(Product_id=product_id)

            
                    total_amount = int(qty) * add_product_dt.price
                    print(total_amount)
                    # Create cart item
                    cart=addcart(

                        Product_id=product_id,
                    
                        user_uid =user_id ,
                        sku_code=add_product_dt.sku_code ,
                        title=add_product_dt.title,
                        color =add_product_dt.color,
                    
                        img1= add_product_dt.img1,
                        qty =qty, 
                        size =size,
                        price =add_product_dt.price,
                        
                        mrp =add_product_dt.mrp,
                        total_amount = str(total_amount),  # Save calculated total amount as an integer
                    
                        total_qty = qty,
                    
                    
                    
                    )
                    cart.save()
                    return redirect('productdt', product_id=product_id)
                
                except:
                    add_buy_dt = Productdt.objects.get(Product_id=buy_id)

                    # Calculate total amount based on quantity and price
                    total_amount = int(qty) * add_buy_dt.price
                    print(total_amount)

                    # Create cart item
                    cart=addcart(

                        Product_id=buy_id,
                    
                        user_uid =user_id ,
                        sku_code=add_buy_dt.sku_code ,
                        title=add_buy_dt.title,
                        color =add_buy_dt.color,
                        img1= add_buy_dt.img1,
                        qty =qty, 
                        size =size,
                        price =add_buy_dt.price,
                        mrp =add_buy_dt.mrp,
                        total_amount=total_amount,  # Save calculated total amount as an integer
                       
                        total_qty=qty,
                    
                        
                    
                    
                    
                    )
                    cart.save()
                #  return HttpResponse('test')
                    return redirect('/reseller/cart/', product_id=buy_id)

          #  return HttpResponse('test')

            
        # Fetch product details again for rendering
       # get_product_dt = Productdt.objects.filter(Product_id=product_id)

        # Pass the product details to the template
      #  return render(request, 'Product page.html', {'product': get_product_dt, 'msg': 'Product is added to cart'})

    except:
       return redirect('/reseller/?message=Please login') 

###################################### ADDCART METHOD CLOSE #######################################################     
    
###################################### CART METHOD START  #########################################################     
def cart(request):
    try:
        user_id = request.session.get('user_uid')
        print(user_id )
        user = User.objects.get(user_uid=user_id)

        
        cart_product = addcart.objects.filter(user_uid=user_id)
    
        if request.method == 'POST':
            margin = request.POST.get('margin')
            print('margin',margin)
            return redirect("/reseller/check_out/")
        
        price = 0
        qty1 = 0
        for p in cart_product:
            t = (p.total_amount)
            price = price + float(t)
            qty1 = qty1 + int(p.qty)
        

        data={
        
            'cart_product':cart_product,
            'total_price':price,
            'qty1':qty1
        }

        return render(request,'reseller/Shopping Cart.html',data)
    except:
      return redirect('/reseller/?message=Please login') 


from django.shortcuts import redirect, get_object_or_404

###################################### CART METHOD CLOSE  #########################################################     

###################################### REMOVE PRODUCT METHOD START ################################################  
def remove_product(request):
    try:
        user_id = request.session.get('user_uid')
        print(user_id )
        user = User.objects.get(user_uid=user_id)
        print(user )
        if request.method == 'POST':
            remove_product_id = request.POST.get('remove')
        
            remove_id = get_object_or_404(addcart, id=remove_product_id)
            remove_id.delete()
            return redirect('/reseller/cart/')
   #return  HttpResponse('remove product')
    except:
       return redirect('/reseller/?message=Please login') 


###################################### CART METHOD CLOSE ######################################################### 

###################################### CHECKOUT METHOD  START ####################################################   
def check_out(request):
    try:
        user_id = request.session.get('user_uid')
        print(user_id )
        user = User.objects.get(user_uid=user_id)
        print(user)
       
        cart_products = addcart.objects.filter(user_uid=user_id)
        
        
        if request.method == 'POST':
            
            r = request.POST.get('reselling')
            if r == 'yes' :
                margin = request.POST.get('margin')
                print('margin',margin)  
                for p in cart_products:
                    m = int(margin) - p.price 
                #    m = margin - p.price        
                dt = {
                    'margin':margin,
                    'm':m
                }  
            else:
                 dt = {
                    'margin':0,
                    'm':0, 
                }   

            # Redirect to a confirmation page or any other desired page
     #   return redirect('/confirm_order/')  # Adjust the URL name as needed
             
        return render(request, 'reseller/check_out_page.html',dt)  # Render the checkout page if not POST request

    
      #  return render(request, 'check_out page.html')
    except:
       return redirect('/reseller/?message=Please login') 




def confirm_order(request):
    try:
      
        user_id = request.session.get('user_uid')
        print('user_id',user_id)
        user = User.objects.get(user_uid = user_id )
        print('user',user)
    #    if request.method == 'POST':
            # margin = request.POST.get('margin')
            # print('margin',margin) 
        
      
            
        cart_products = addcart.objects.filter(user_uid=user_id)
          
        if 'm' in request.GET:
            margin=request.GET['m']   
        else:
            margin = 0     
        if request.method == 'POST':
              
           
            firstName = request.POST.get('firstName')
            phone_number = request.POST.get('phone')
            address = request.POST.get('address')
            pincode = request.POST.get('pincode')
            landmark = request.POST.get('landmark')
            state = request.POST.get('state')
            
            order_id = str(uuid.uuid4().hex[:10])
            order_date = datetime.now()
           
            for o in cart_products:
                product_id = o.Product_id

           

                
                order = Order(
                        email= user.email , 
                        user_uid=user_id,  
                        Product_id=product_id,
                        price=o.price,
                        total_qty=o.total_qty,
                        name=firstName,
                        phone_number=phone_number,
                        address=address,
                        pincode=pincode,
                        landmark=landmark,
                        state=state,
                        order_id=order_id,
                        order_date=order_date,
                        order_status="New",
                        tracking_id="",
                        tracking_link="",
                        reselling_amount = int(margin),
                        resell_margin = int(margin) - o.price,
                        img1 = o.img1
                            



                            
                        
                            

                    )
                order.save()
                last_id = order.id
             #   print('last id = ', last_id)
                    #  return HttpResponse('Order data saved successfully')  
                return redirect(f'/reseller/order_detail_page/?id={last_id}')
            
              
                # return redirect('/')

        return render(request, 'reseller/check_out_page.html')  # Render the confirm order page

    except:
         return redirect('/reseller/')

###################################### CHECKOUT METHOD  CLOSE ####################################################     
    
###################################### ORDER DETAIL METHOD  START ###############################################    

def order_detail_page(request):
    try:
        user_id = request.session.get('user_uid')
        user = User.objects.get(user_uid=user_id)
        lid=request.GET['id'] 
        print(user )

        orders=Order.objects.filter(user_uid=user_id, id = lid )
     #   email = request.session.get('email')
     #   print("email_id",email)
     
        
        cart_product = addcart.objects.filter(user_uid=user_id)
        print(cart_product)
        cart_product.delete()
       
      
     
        return render(request, 'reseller/order_detailpage.html', {'orders': orders,'error':'Thank you for shoppiong with us!'})

    
    except:
  
       return redirect('/reseller/')
    
###################################### ORDER DETAIL METHOD  CLOSE ############################################### 

###################################### MYPAYMENTS  METHOD  START ################################################  

def mypayments(request):
    # try:
        user_id = request.session.get('user_uid')
        print("User ID:", user_id)
        user = User.objects.get(user_uid=user_id)
        
        # orders = Order.objects.exclude(user_uid=user_id)
    
    
        orders = Order.objects.filter(user_uid=user_id).exclude(reselling_amount=0)
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        print(cart_count )
        
    
        return render(request, 'reseller/mypayments.html', {'orders': orders,'cart_count': cart_count,})

    # except:
    #    return redirect('/reseller/?message=Please login') 


###################################### MYPAYMENTSMETHOD  CLOSE ###############################################      
    
###################################### PROFILE METHOD  START #################################################
def profile(request):
    
    try:
        user_id = request.session.get('user_uid')
        user_data = User.objects.filter(user_uid=user_id)
     
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()

      
        total_order_count = Order.objects.filter(user_uid=user_id).count()
        print('total_order_count',total_order_count)

        new_order_count = Order.objects.filter(user_uid=user_id, order_status='New').count()
        print('new_order_count',new_order_count)

        delivered_order_count = Order.objects.filter(user_uid=user_id, order_status='delivered').count()
        print('delivered_order_count',delivered_order_count)

        shipped_order_count = Order.objects.filter(user_uid=user_id, order_status='Shipped').count()
        print('shipped_order_count',shipped_order_count)

        canceled_order_count = Order.objects.filter(user_uid=user_id, order_status='Canceled').count()
        print('canceled_order_count',canceled_order_count)

        data = {
            'user_data': user_data,
            'cart_count': cart_count,
            'total_order_count': total_order_count,
            'new_order_count': new_order_count,
            'delivered_order_count': delivered_order_count,
            'shipped_order_count': shipped_order_count,
            'canceled_order_count': canceled_order_count
        }
        return render(request, 'reseller/profile.html', data)
    except:
       return redirect('/reseller/?message=Please login') 

###################################### PROFILE METHOD CLOSE  ####################################################      


###################################### ALL ORDER METHOD       ##################################################   
def all_orders(request):
    try:
        user_id = request.session.get('user_uid')
        print('user_id',user_id)
        all_orders = Order.objects.all().order_by('-id')
        print('all_orders',all_orders)
        
    
        total_order_count = all_orders.count()
        print('total_order_count:',total_order_count)
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        print(cart_count )
        return render(request, 'reseller/all_order.html', {'orders': all_orders, 'total_order_count': total_order_count,'cart_count': cart_count,})
        
                
    except:
       return redirect('/reseller/?message=Please login') 
     
###################################### NEW ORDER METHOD ############################################### 

def new_orders(request):
    try:
        user_id = request.session.get('user_uid')
        print('user_id', user_id)
        new_orders = Order.objects.filter(user_uid=user_id, order_status="New").order_by('-id')
        print('new_orders',new_orders)
        new_order_count = new_orders.count()
        print('new_order_count:', new_order_count)
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        print(cart_count )
        return render(request, 'reseller/all_order.html', {'orders': new_orders, 'new_order_count': new_order_count,'cart_count': cart_count,})

    except:
       return redirect('/reseller/?message=Please login') 
###################################### DELIVER ORDER METHOD ###############################################   
def delivered_orders(request):
    try:
    
        user_id = request.session.get('user_uid')
        print('user_id',user_id)
        delivered_orders = Order.objects.filter(user_uid=user_id, order_status='delivered').order_by('-id')
        print('delivered_orders:',delivered_orders)
        
        delivered_order_count = delivered_orders.count()
        print('delivered_order_count:',delivered_order_count)
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        print(cart_count )
        return render(request, 'reseller/all_order.html', {'orders': delivered_orders, 'delivered_order_count': delivered_order_count,'cart_count': cart_count,})

    except:
       return redirect('/reseller/?message=Please login') 
    
###################################### SHIPPED ORDER METHOD ###############################################   
    
def shipped_orders(request):
    try:
        user_id = request.session.get('user_uid')
        print('user_id',user_id)
    
        shipped_orders = Order.objects.filter(user_uid=user_id, order_status='Shipped').order_by('-id')
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        print(cart_count )
        
        return render(request, 'reseller/all_order.html', {'orders': shipped_orders , 'cart_count': cart_count,'cart_count': cart_count,})

    except:
       return redirect('/reseller/?message=Please login') 

###################################### CANCEL ORDER METHOD ###############################################  

def cancel_orders(request):
    try:
        user_id = request.session.get('user_uid')
        canceled_orders = Order.objects.filter(user_uid=user_id, order_status='Canceled').order_by('-id')
        print('canceled_orders:',canceled_orders)
        

        canceled_order_count = canceled_orders.count()
        print('canceled_order_count',canceled_order_count)
        cart_product = addcart.objects.filter(user_uid=user_id)
        cart_count = cart_product.count()
        print(cart_count )
        
        return render(request, 'reseller/all_order.html', {'orders': canceled_orders, 'canceled_order_count': canceled_order_count})
    except:
       return redirect('/reseller/?message=Please login') 

def footer(request):
    try:
        return render(request,"footer.html") 
    except:
       return redirect('/reseller/?message=Please login') 
# ##############################################
# test

<<<<<<< HEAD
# def youtube(request):
#     return render(request,'you tube clone.html')

=======
# test

# def youtube(request):
#     return render(request,'you tube clone.html')

>>>>>>> e9aee8372386e4c0b29cea0ce6721898513a1586
# def video(request):
#     return render(request,'Video-play.html')
# def meesho(request):
#     return render(request,'meesho.html')
# def home(request):
<<<<<<< HEAD
#     return HttpResponse('welcome to homepage')  # Udaharan view function
=======
#     return HttpResponse('welcome to homepage')  # Udaharan view function
>>>>>>> e9aee8372386e4c0b29cea0ce6721898513a1586
