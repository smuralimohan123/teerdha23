from django.shortcuts import render,redirect
import requests   
from rest_framework.views import APIView
from rest_framework.response import Response
from .serialization import TaxiFareSerializer,Navigationdata,Carouseldata
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
from django.http import HttpResponse

import requests
from .models import *
from rest_framework.decorators import api_view
class TaxiFareAPIView(APIView):
    def get(self, request):
        serializer = TaxiFareSerializer(data=request.query_params)
        if serializer.is_valid():
            data = serializer.validated_data
            url = "https://taxi-fare-calculator.p.rapidapi.com/search-geo"
            headers = {
                "X-RapidAPI-Key": "00dbe9f6fbmsh2e9eadc0a067640p18d2d8jsna36ab702d877",
                "X-RapidAPI-Host": "taxi-fare-calculator.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=data)
            return Response(response.json())
        return Response(serializer.errors, status=400)


class add_navigation_list(GenericAPIView,CreateModelMixin):
    queryset=Naviagtion_bar.objects.all()
    serializer_class=Navigationdata
    def post(self,request):
        return self.create(request)
class Update_navigation_list(GenericAPIView,UpdateModelMixin):
    queryset=Naviagtion_bar.objects.all()
    serializer_class=Navigationdata
    def put(self,request,**kwargs):
        return self.update(request, ** kwargs)
class Remove_navigation_list(GenericAPIView,DestroyModelMixin):
    queryset=Naviagtion_bar.objects.all()
    serializer_class=Navigationdata
    def delete(self,request, **kwargs):
        return self.destroy(request, **kwargs)
class Table_navigation_list(GenericAPIView,RetrieveModelMixin):
    queryset=Naviagtion_bar.objects.all()
    serializer_class=Navigationdata
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
class Navigationlist(GenericAPIView,ListModelMixin):
    queryset=Naviagtion_bar.objects.all()
    serializer_class=Navigationdata
    def get(self,request):
        return self.list(request)
    

    
class add_carousel_list(GenericAPIView,CreateModelMixin):
    queryset=Home_carousel.objects.all()
    serializer_class=Carouseldata
    def post(self,request):
        return self.create(request)
class Update_carousel_list(GenericAPIView,UpdateModelMixin):
    queryset=Home_carousel.objects.all()
    serializer_class=Carouseldata
    def put(self,request,**kwargs):
        return self.update(request, ** kwargs)
class Remove_carousel_list(GenericAPIView,DestroyModelMixin):
    queryset=Home_carousel.objects.all()
    serializer_class=Carouseldata
    def delete(self,request, **kwargs):
        return self.destroy(request, **kwargs)
class Table_carousel_list(GenericAPIView,RetrieveModelMixin):
    queryset=Home_carousel.objects.all()
    serializer_class=Carouseldata
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
class Carousel_list(GenericAPIView,ListModelMixin):
    queryset=Home_carousel.objects.all()
    serializer_class=Carouseldata
    def get(self,request):
        return self.list(request)
    
def Carousel_home(request):
    carousel=Home_carousel.objects.all()
    return render(request,"carousel_home.html",{'carousel':carousel})
    
def Ticketbooking(request):
    return render(request,"ticketbooking.html")
def footer(request):
    return render(request,"footer.html")
def contactus(request):
    if request.method=="POST":
    
        Name=request.POST['Name']
        Phonenumber=request.POST['Phonenumber']
        Email=request.POST['Email']
        Message=request.POST['Message']
        Status=request.POST['Status']

        msg=Contact(Name=Name,Phonenumber=Phonenumber,Email=Email,Message=Message,Status=Status)
        msg.save()
        return redirect("/contactus")
    return render(request,"contact_form.html")

    
def contact_table(request):
    contact_info=Contact.objects.all()
    return render(request,"contact_table.html",{'contact_info':contact_info})
 
def teerdha_page(request):
    return render(request,"base.html")



    ####     navbar  ####

def navbar_page(request):
    if request.method=="POST":
        photo=request.FILES.get('photo')
        title=request.POST['title']
        url=request.POST['url']
        icon=request.POST['icon']
        nav=navbar(photo=photo, title=title, url=url, icon=icon)
        nav.save()
        return HttpResponse ("record is inserted")
    return render(request,"navbar_insert.html")

def navbar_table(request):
    if request.method=="GET":
       nav=navbar.objects.all()
    return render(request,"nav.html",{'nav':nav})


##...dashboard...##

         
##... Flights  dashboard...##

def flightoffers_insertform(request):
    if request.method == "POST":
        offer=request.POST.get('offer')
        url=request.POST.get('url')
        dt=flights_offerscrudoperations(offer=offer, url=url)
        dt.save()
        return HttpResponse("submitted")
    return render(request,"dashboard_templates/flight_offer.html")


def flight_offertb(request):
    if request.method == "POST":
        offer=request.POST.get('offer')
        url=request.POST.get('url')
        dt=flights_offerscrudoperations(offer=offer, url=url)
        dt.save()
        return redirect("/flight_offertb")
    if request.method == "GET":
        up=flights_offerscrudoperations.objects.all()
        Sidebar=sidebar_dashboard.objects.all()
        nav_item=navbar.objects.all()
    return render(request,"dashboard_templates/flight_offersupdate.html",{'up':up,'Sidebar':Sidebar,'nav_item':nav_item})

def flight2ndpage_insertform(request):
    if request.method == "POST":
        offer=request.POST.get('offer')
        inserturl=request.POST.get('inserturl')
        updateurl=request.POST.get('updateurl')
        ht=flights_2ndpages(offer=offer, inserturl=inserturl,updateurl=updateurl)
        ht.save()
        return HttpResponse("inserted")
    return render(request,"dashboard_templates/flight_2ndpage.html")


def flight_2ndpages(request):
    if request.method == "POST":
        offer=request.POST.get('offer')
        inserturl=request.POST.get('inserturl')
        updateurl=request.POST.get('updateurl')
        ht=flights_2ndpages(offer=offer, inserturl=inserturl,updateurl=updateurl)
        ht.save()
        return redirect("/flight_2ndpages")
    
    if request.method == "GET":
        upt=flights_2ndpages.objects.all()
        Sidebar=sidebar_dashboard.objects.all()
        nav_item=navbar.objects.all()
    return render(request,"dashboard_templates/flight_2ndpagedetails.html",{'upt':upt,'Sidebar':Sidebar,'nav_item':nav_item})


def flight2ndpage_updateform(request):
    if request.method == "POST":
        offer=request.POST.get('offer')
        url=request.POST.get('url')
        ht=flights_2npdpages_update(offer=offer, url=url)
        ht.save()
        return HttpResponse("inserted")
    return render(request,"dashboard_templates/flight_2ndpageupdate.html")



def flight_2ndpagesupdate(request):
    if request.method == "GET":
        upt=flights_2npdpages_update.objects.all()
        Sidebar=sidebar_dashboard.objects.all()
        nav_item=navbar.objects.all()
    return render(request,"dashboard_templates/flight_2ndpageupdates.html",{'upt':upt,'Sidebar':Sidebar,'nav_item':nav_item})


    ###       Buses  dashboard   ######
   
def busoffers_insertform(request):
    if request.method == "POST":
        offer=request.POST.get('offer')
        url=request.POST.get('url')
        dk=buses_offerscrudoperations(offer=offer, url=url)
        dk.save()
        return HttpResponse("submitted")
    return render(request,"dashboard_templates/flight_offer.html")



def buses_offertb(request):
    if request.method == "POST":
        offer=request.POST.get('offer')
        url=request.POST.get('url')
        op=buses_offerscrudoperations(offer=offer, url=url)
        op.save()
        return redirect("/buses_offertb")
    
    if request.method == "GET":
        op=buses_offerscrudoperations.objects.all()
        Sidebar=sidebar_dashboard.objects.all()
        nav_item=navbar.objects.all()
    return render(request,"dashboard_templates/buses_offersupdate.html",{'op':op,'Sidebar':Sidebar,'nav_item':nav_item})


def buses2ndpage_insertform(request):
    if request.method == "POST":
        offer=request.POST.get('offer')
        inserturl=request.POST.get('inserturl')
        updateurl=request.POST.get('updateurl')
        ht=buses_2ndpages(offer=offer, inserturl=inserturl,updateurl=updateurl)
        ht.save()
        return HttpResponse("inserted")
    return render(request,"dashboard_templates/buses_2ndpage.html")


def bus_2ndpages(request):
    if request.method == "GET":
        upt=buses_2ndpages.objects.all()
        Sidebar=sidebar_dashboard.objects.all()
        nav_item=navbar.objects.all()
    return render(request,"dashboard_templates/buses_2ndpagedetails.html",{'upt':upt,'Sidebar':Sidebar,'nav_item':nav_item})


          ###       Cabs  dashboard   ######

def cabs_insert_dashboard(request):
    if request.method == "POST":
        offer=request.POST.get('offer')
        url=request.POST.get('url')
        dt=cabs_offerscrud_dashboard(offer=offer, url=url)
        dt.save()
        return HttpResponse("submitted")
    return render(request,"dashboard_templates/cabdb_offer.html")

def cabs_table_dashboard(request):
    if request.method == "POST":
        offer=request.POST.get('offer')
        url=request.POST.get('url')
        dt=cabs_offerscrud_dashboard(offer=offer, url=url)
        dt.save()
        return redirect("/cabs_table_dashboard")
    
    if request.method == "GET":
        up=cabs_offerscrud_dashboard.objects.all()
        Sidebar=sidebar_dashboard.objects.all()
        nav_item=navbar.objects.all()
    return render(request,"dashboard_templates/cab_dashboardupdate.html",{'up':up,'Sidebar':Sidebar,'nav_item':nav_item})
   

#####           2nd pages           ######

def cabs_insert_2ndpagedb(request):
    if request.method == "POST":
        offer = request.POST.get('offer')
        url_insert = request.POST.get('url_insert')
        offer_data =request.POST.get('offer_data')
        url_update = request.POST.get('url_update')
        dt = cabs_secondpage_dashboard(offer=offer, url_insert=url_insert, url_update=url_update, offer_data=offer_data)
        dt.save()
        return HttpResponse("submitted")
    return render(request, "cabdb_offer2ndpage.html")



def cabs_table_2ndpagedb(request):
    if request.method == "POST":
        offer = request.POST.get('offer')
        url_insert = request.POST.get('url_insert')
        offer_data =request.POST.get('offer_data')
        url_update = request.POST.get('url_update')
        dt = cabs_secondpage_dashboard(offer=offer, url_insert=url_insert, url_update=url_update, offer_data=offer_data)
        dt.save()
        return redirect("/cabs_table_2ndpagedb")

    if request.method == "GET":
        up = cabs_secondpage_dashboard.objects.all()
        Sidebar=sidebar_dashboard.objects.all()
        nav_item=navbar.objects.all()
    return render(request, "dashboard_templates/cab_dashboard2ndpage.html", {'up': up,'Sidebar':Sidebar,'nav_item':nav_item})



          ###       Hotels  dashboard   ######

def hoteloffers_insertform(request):
    if request.method == "POST":
        offer=request.POST.get('offer')
        url=request.POST.get('url')
        dk=hotels_offerscrudoperations(offer=offer, url=url)
        dk.save()
        return HttpResponse("submitted")
    return render(request,"dashboard_templates/hotels_offer.html")

def hotels_offertb(request):
    if request.method == "POST":
        offer=request.POST.get('offer')
        url=request.POST.get('url')
        dk=hotels_offerscrudoperations(offer=offer, url=url)
        dk.save()
        return redirect("/hotels_offertb")
    
    if request.method == "GET":
        pt=hotels_offerscrudoperations.objects.all()
        Sidebar=sidebar_dashboard.objects.all()
        nav_item=navbar.objects.all()
    return render(request,"dashboard_templates/hotels_offersupdate.html",{'pt':pt,'Sidebar':Sidebar,'nav_item':nav_item})

   
def hotel2ndpage_insertform(request):
    if request.method == "POST":
        offer=request.POST.get('offer')
        inserturl=request.POST.get('inserturl')
        updateurl=request.POST.get('updateurl')
        ht=hotels_2ndpages(offer=offer, inserturl=inserturl,updateurl=updateurl)
        ht.save()
        return HttpResponse("inserted")
    return render(request,"hotel_2ndpage.html")


def hotel_2ndpages(request):
    if request.method == "POST":
        offer=request.POST.get('offer')
        inserturl=request.POST.get('inserturl')
        updateurl=request.POST.get('updateurl')
        ht=hotels_2ndpages(offer=offer, inserturl=inserturl, updateurl=updateurl)
        ht.save()
        return redirect("/hotel_2ndpages")
    
    if request.method == "GET":
        upt=hotels_2ndpages.objects.all()
        Sidebar=sidebar_dashboard.objects.all()
        nav_item=navbar.objects.all()
    return render(request,"dashboard_templates/hotel_2ndpagedetails.html",{'upt':upt,'Sidebar':Sidebar,'nav_item':nav_item})


####  dashboard  sidebar   #####

def admin_insertforms(request):
    if request.method == "POST":
        title = request.POST['title']
        url = request.POST['url']
        icon = request.POST['icon']
        subdivision = request.POST['subdivision']   
        xy = sidebar_dashboard(title=title, url=url, icon=icon, subdivision=subdivision)
        xy.save()
    return render(request, "dashboard_templates/admin_insert.html")

def sidebar_retrieve(request):
    if request.method== "GET":
        Sidebar=sidebar_dashboard.objects.all()
        nav_item=navbar.objects.all()
    return render(request,"dashboard_templates/sidebar_ret.html",{'Sidebar':Sidebar, 'nav_item':nav_item}) 
    
  
def airports(request):
            
    url = "https://booking-com.p.rapidapi.com/v1/hotels/photos"

    querystring = {"hotel_id":"1377073","locale":"en-gb"}

    headers = {
        "x-rapidapi-key": "b54b11ee9cmsh7bbd272076daabbp1446aejsn5ffa3e29f473",
        "x-rapidapi-host": "booking-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    virat=response.json()

    return render(request,"any_data.html",{'virat': virat})



# views.py
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render, redirect

def password_reset_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            confirm_password = form.cleaned_data['confirm_password']

            # Perform password change logic here
            user = request.user  # Assuming the user is authenticated
            if user.check_password(old_password) and new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)  # Important to maintain session

                # Redirect to success page or any other page
                return redirect('password_reset_success')
            else:
                # Handle invalid password change attempt
                # You might want to add error messages here
                pass  # Handle this case as per your requirements
    else:
        form = PasswordResetForm()

    return render(request,'dashboard_templates/password_reset.html', {'form': form})



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import Profiles
from django.shortcuts import HttpResponse
from django.contrib.auth.hashers import make_password

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def ajax_test(request):
    if is_ajax(request=request):
        user=request.user
        password=request.POST.get('password')
        newpassword=request.POST.get('newpassword')
        print(password)
        obj=User.objects.get(username=user)
        if obj.check_password(password):
            obj.set_password(newpassword)
            obj.save()
            return JsonResponse({'status': 'success', 'message': 'updated successfully'})
        else:
            return JsonResponse({'status': 'failed', 'message': ' invalid password'})


@never_cache
@login_required
def dashboard(request):
    if request.method=="POST":
        user_profile=Profiles.objects.get(user=request.user)
        image=request.FILES.get("image")
        email=request.POST.get("email")
        mobile=request.POST.get("mobile_number")
        print(email,mobile,image)
        if image:
            user_profile.image=image
        if email:
            user_profile.email=email
        if mobile:
            user_profile.mobile_number=mobile
        user_profile.save()
        

    Sidebar=sidebar_dashboard.objects.all()
    nav_item=navbar.objects.all()
    profile = Profiles.objects.get(user=request.user)
    return render(request, 'dashboard_templates/admin.html',{'Sidebar':Sidebar, 'profile':profile,'nav_item':nav_item})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'dashboard_templates/login.html')

def logout_view(request):
    return redirect('/login/')


from django.http import JsonResponse

@login_required
def update_profile(request):
    profile = Profiles.objects.get(user=request.user)
    
    if request.method == 'POST':
        image = request.FILES.get('image')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        print(email,mobile_number,image)
        if image:
            profile.image = image
        if email:
            profile.email = email
        if mobile_number:
            profile.mobile_number = mobile_number
        
        profile.save()
        
        # Return updated profile data as JSON
        # response_data = {
        #     'image_url': profile.image.url,
        #     'email': profile.email,
        #     'mobile_number': profile.mobile_number
        # }
        # return JsonResponse(response_data)
    
    return render(request, 'dashboard_templates/user_profile.html', {'profile': profile})  



