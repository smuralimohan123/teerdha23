from django.shortcuts import render,redirect
from .models import *
from .serialization import *
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from django.http import HttpResponse
import requests
from django.conf import settings



############### cab search form ################
def cab(request):
    if request.method == "POST":
        from_city = request.POST.get('from_city')
        to_city = request.POST.get('to_city')
        departure_date = request.POST.get('departure_date')
        return_date = request.POST.get('return_date')
        pickup_time = request.POST.get('pickup_time')
        drop_time = request.POST.get('drop_time')
        k= CabBooking(from_city=from_city,to_city=to_city,departure_date=departure_date,return_date= return_date,pickup_time=pickup_time,drop_time=drop_time)
        k.save()
        return HttpResponse("response is inserted")
    return render(request,"cab_templates/cabsearch.html")

################## cab offer cards#####################
class cabsapi(generics.ListCreateAPIView):
    queryset=cab_cards.objects.all()
    serializer_class=cab_serialization

class cab_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=cab_cards.objects.all()
    serializer_class=cab_serialization

def cab_main(request):
    nav=navbar.objects.all()
    if request.method=="GET":
        ad=requests.get(settings.API_URL+"/cab_insert/")
        res=ad.json()
        k3 = cabwhycontents.objects.all()
        b = cab_faq.objects.all()
        return render(request,"cab_templates/cabsearch.html",{'nav':nav,'res':res,'k3':k3,'b':b})
  
############# 2nd page for 1st card ####################

class cabcard1(generics.ListCreateAPIView):
    queryset=cab_festive.objects.all()
    serializer_class=festive_serialization

class festive_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=cab_festive.objects.all()
    serializer_class=festive_serialization

    
def festive_main(request):
    if request.method == "GET":
        ad = requests.get(settings.API_URL+"/festive_insert/")
        res = ad.json()
        return render(request, "cab_templates/festive.html", {'res': res})



############# 2nd page for 2nd card card ####################

class cabcard2(generics.ListCreateAPIView):
    queryset=cab_rental.objects.all()
    serializer_class=rental_serialization

class rental_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=cab_rental.objects.all()
    serializer_class=rental_serialization


def rental_main(request):
    if request.method == "GET":
        ad = requests.get(settings.API_URL+"/rental_insert/")
        res = ad.json()
        return render(request, "cab_templates/rental_card.html", {'res': res})



############# 2nd page for 3rd card ####################

class cabcard3(generics.ListCreateAPIView):
    queryset=cab_anytime.objects.all()
    serializer_class=anytime_serialization

class anytime_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=cab_anytime.objects.all()
    serializer_class=anytime_serialization


def anytime_main(request):
    if request.method=="GET":
        ad=requests.get(settings.API_URL+"/anytime_insert/")
        res=ad.json()
        return render(request,"cab_templates/anytime_card.html",{'res':res})



############# 2nd page for 4th card ####################

class cabcard4(generics.ListCreateAPIView):
    queryset=cab_ride.objects.all()
    serializer_class=ride_serialization

class ride_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=cab_ride.objects.all()
    serializer_class=ride_serialization


def ride_main(request):
    if request.method=="GET":
        ad=requests.get(settings.API_URL+"/ride_insert/")
        res=ad.json()
        return render(request,"cab_templates/ride_card.html",{'res':res})



############# 2nd page for 5th card ####################

class cabcard5(generics.ListCreateAPIView):
    queryset=cab_familyfun.objects.all()
    serializer_class=familyfun_serialization

class familyfun_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=cab_familyfun.objects.all()
    serializer_class=familyfun_serialization


def familyfun_main(request):
    if request.method=="GET":
        ad=requests.get(settings.API_URL+"/familyfun_insert/")
        res=ad.json()
        return render(request,"cab_templates/familyfun_card.html",{'res':res})


############# 2nd page for 6th card ####################

class cabcard6(generics.ListCreateAPIView):
    queryset=cab_easy.objects.all()
    serializer_class=easy_serialization

class easy_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=cab_easy.objects.all()
    serializer_class=easy_serialization


def easy_main(request):
    if request.method=="GET":
        ad=requests.get(settings.API_URL+"/easy_insert/")
        res=ad.json()
        return render(request,"cab_templates/easy_card.html",{'res':res})


############# 2nd page for 7th card ####################

class cabcard7(generics.ListCreateAPIView):
    queryset=cab_offer_card.objects.all()
    serializer_class=offer15_serialization

class offer15_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=cab_offer_card.objects.all()
    serializer_class=offer15_serialization


def offer15_main(request):
    if request.method=="GET":
        ad=requests.get(settings.API_URL+"/offer15_insert/")
        res=ad.json()
        return render(request,"cab_templates/offer15_card.html",{'res':res})


############# 2nd page for 8th card ####################

class cabcard8(generics.ListCreateAPIView):
    queryset=cab_paytm_card.objects.all()
    serializer_class=paytm_card_serialization

class paytm_card_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=cab_paytm_card.objects.all()
    serializer_class=paytm_card_serialization


def paytm_card_main(request):
    if request.method=="GET":
        ad=requests.get(settings.API_URL+"/paytm_card_insert/")
        res=ad.json()
        return render(request,"cab_templates/paytm_card.html",{'res':res})

##########################  why choose content for cabs #######################

def WhyChoose(request):
    if request.method == "POST":
        ctitle = request.POST.get('ctitle')
        heading1 = request.POST.get('heading1')
        k3 = cabwhycontents(ctitle=ctitle, heading1=heading1)
        k3.save()
        return redirect("/cabs_whychoose")
    return render(request,"cab_templates/WhyChoose_insert.html")

def WhyChoosecard(request):
    if request.method == "GET":
        k3 = cabwhycontents.objects.all()
    return render(request,"cab_templates/cabsearch.html", {'k3': k3})

############ CRUD OPERATIONS FOR WHY CHOOSE US  #########################



def WhyChoose_crud_update(request,id):
    if request.method == "POST":
        ctitle = request.POST['ctitle']
        heading1 = request.POST['heading1']
        k3=cabwhycontents.objects.get(id=id)
        k3.ctitle=ctitle
        k3.heading1 = heading1
        k3.save()
        return redirect("/cabs_whychoose")
    return render(request,"cab_templates/WhyChoose_update1.html")

def  WhyChoose_crud_del(request,id):
        k3=cabwhycontents.objects.get(id=id)
        k3.delete()
        return redirect("/cabs_whychoose")

def WhyChoose_crud_edit(request,id):
    if request.method=="GET":
        k3=cabwhycontents.objects.get(id=id)
    return render(request,"cab_templates/WhyChoose_update1.html",{'k3':k3})


def cabs_whychoose(request):
    if request.method == "POST":
        ctitle = request.POST.get('ctitle')
        heading1 = request.POST.get('heading1')
        k3 = cabwhycontents(ctitle=ctitle, heading1=heading1)
        k3.save()
        return redirect("/cabs_whychoose")

    if request.method == "GET":
        k3 = cabwhycontents.objects.all()
        Sidebar=sidebar_dashboard.objects.all()
        nav_item=navbar.objects.all()
    return render(request,"cab_templates/WhyChoose_table1.html",{'k3': k3,'Sidebar':Sidebar, 'nav_item':nav_item})




############################# cab faq ############################


def cabfaq_upd(request):
    if request.method == "POST":
        content = request.POST.get('content',default='')
        Title = request.POST.get('Title',default='')
        description = request.POST.get('description', default='')
        b = cab_faq(content=content,Title=Title, description=description)
        b.save()
        return redirect("/cabfaq_home")
    return render(request, "cab_templates/cabfaqupd1.html")


############ CRUD OPERATIONS FOR faqs #########################


def cabfaq_crud_update(request,id):
    if request.method == "POST":
        content = request.POST['content']
        Title = request.POST['Title']
        description = request.POST['description']
        b=cab_faq.objects.get(id=id)
        b.content=content
        b.Title = Title
        b.description = description
        b.save()
        # return redirect("/homepage")
        return redirect("/cabfaq_home")
    return render(request,"cab_templates/cabcrudupdate.html")

def cabfaq_crud_del(request,id):
        b=cab_faq.objects.get(id=id)
        b.delete()
        return redirect("/cabfaq_home")
def cabfaq_crud_edit(request,id):
    if request.method=="GET":
        b=cab_faq.objects.get(id=id)
    return render(request,"cab_templates/cabcrudupdate.html",{'b':b})


def cabfaq_home(request):
    if request.method == "POST":
        content = request.POST.get('content',default='')
        Title = request.POST.get('Title',default='')
        description = request.POST.get('description', default='')
        b = cab_faq(content=content,Title=Title, description=description)
        b.save()
        return redirect("/cabfaq_home")

    if request.method == "GET":
        b = cab_faq.objects.all()
        Sidebar=sidebar_dashboard.objects.all()
        nav_item=navbar.objects.all()
    return render(request, "cab_templates/cabfaqdelete.html",{'b': b,'Sidebar':Sidebar, 'nav_item':nav_item})
