from django.shortcuts import render,redirect
from .models import *
from .serialization import *
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from django.http import HttpResponse
import requests
from django.conf import settings


########## bus_trending offers cards  ############


class busapi(generics.ListCreateAPIView):
    queryset=bus_offercards.objects.all()       
    serializer_class=bus_serialization

class bus_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_offercards.objects.all()
    serializer_class=bus_serialization


def bus_main(request):
    if request.method=="GET":
        nav=navbar.objects.all()
        ad=requests.get(settings.API_URL+"/bus_home/")
        res=ad.json()
        k2= bus_whychoose.objects.all()
        k1= bus_faq.objects.all()
        return render(request,"bus_templates/d.html",{'nav':nav,'res':res,'k2':k2,'k1':k1})
    
########### why choose us   ###############

def bus_whychoose_form(request):
    if request.method=="POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        k2=bus_whychoose(title=title, content=content)
        k2.save()
        return redirect("/bus_whychoose_op")   
    return render(request,"bus_templates/whychoose_ins.html")


def bus_whychoose_content(request):
    if request.method=="GET":
        k2=bus_whychoose.objects.all()
    return render(request,"bus_templates/whychoose_ins.html",{'k2':k2})

def bus_whychoose_update(request,id):
    if request.method=="POST":
        title=request.POST['title']
        content=request.POST['content'] 
        k2=bus_whychoose.objects.get(id=id)
        k2.title=title
        k2.content=content
        k2.save()
        return redirect("/bus_whychoose_op")
    return render(request,"bus_templates/whychoose_up.html")

def bus_whychoose_delete(request,id):
        k2=bus_whychoose.objects.get(id=id)
        k2.delete()
        return redirect("/bus_whychoose_op")
        return render(request,"bus_templates/whychoose_del.html")


def bus_whychoose_edit(request,id):
    if request.method=="GET":
        k2=bus_whychoose.objects.get(id=id)
    return render(request,"bus_templates/whychoose_up.html",{'k2':k2})

def bus_whychoose_upd(request):
    if request.method=="GET":
        k2=bus_whychoose.objects.all()
    return render(request,"bus_templates/whychoose_up.html",{'k2':k2})


def bus_whychoose_op(request):

    if request.method=="POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        k2=bus_whychoose(title=title, content=content)
        k2.save()
        return redirect("/bus_whychoose_op") 

    if request.method=="GET":
        k2=bus_whychoose.objects.all()
        Sidebar=sidebar_dashboard.objects.all()
        nav_item=navbar.objects.all()
    return render(request,"bus_templates/whychoose_del.html",{'k2': k2,'Sidebar':Sidebar, 'nav_item':nav_item})

       
############ teerdha faq  #################

   
def bus_faq_form(request):
    if request.method=="POST":
        description1=request.POST.get('description1')
        description2=request.POST.get('description2')
        k1=bus_faq(description1=description1, description2=description2)
        k1.save()
        return redirect("/bus_faq_op")   
    return render(request,"bus_templates/faq_ins.html")


def bus_faq_content(request):
    if request.method=="GET":
        k1=bus_faq.objects.all()
    return render(request,"bus_templates/faq_ins.html",{'k1':k1})



def bus_faq_update(request,id):
    if request.method=="POST":
        description1=request.POST['description1']
        description2=request.POST['description2'] 
        k1=bus_faq.objects.get(id=id)
        k1.description1=description1
        k1.description2=description2
        k1.save()
        return redirect("/bus_faq_op")
    return render(request,"bus_templates/faq_up.html")


def bus_faq_delete(request,id):
        k1=bus_faq.objects.get(id=id)
        k1.delete()
        return redirect("/bus_faq_op")
        return render(request,"bus_templates/faq_del.html")


def bus_faq_edit(request,id):
    if request.method=="GET":
        k1=bus_faq.objects.get(id=id)
    return render(request,"bus_templates/faq_up.html",{'k1':k1})


def bus_faq_upd(request):
    if request.method=="GET":
        k1=bus_faq.objects.all()
    return render(request,"bus_templates/faq_up.html",{'k1':k1})


def bus_faq_op(request):

    if request.method=="POST":
        description1=request.POST.get('description1')
        description2=request.POST.get('description2')
        k1=bus_faq(description1=description1, description2=description2)
        k1.save()
        return redirect("/bus_faq_op") 
     
    if request.method=="GET":
        k1=bus_faq.objects.all()
        Sidebar=sidebar_dashboard.objects.all()
        nav_item=navbar.objects.all()
    return render(request,"bus_templates/faq_del.html",{'k1':k1,'Sidebar':Sidebar, 'nav_item':nav_item})

############  card1  ###############


class bus1api(generics.ListCreateAPIView):
    queryset=bus_weekends1.objects.all()
    serializer_class=bus_weekends1_serialization

class bus_update1(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_weekends1.objects.all()
    serializer_class=bus_weekends1_serialization

class bus0api(generics.ListCreateAPIView):
    queryset=bus_weekends_terms1.objects.all()
    serializer_class=bus_weekends_terms1_serialization

class bus_update0(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_weekends_terms1.objects.all()
    serializer_class=bus_weekends_terms1_serialization


def bus_main1(request):
    if request.method=="GET":
        ad=requests.get(settings.API_URL+"/bus_home1/")
        ad1=requests.get(settings.API_URL+"/bus_home01/")
        res1=ad.json()
        res=ad1.json()
        return render(request,"bus_templates/trendcard1.html",{'res1':res1,'res':res})

###########  card2  #################

class bus2api(generics.ListCreateAPIView):
    queryset=bus_go_table2.objects.all()
    serializer_class=bus_go_table2_serialization

class bus_update2(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_go_table2.objects.all()
    serializer_class=bus_go_table2_serialization


def bus_main2(request):
    if request.method == "GET":
        ad1 = requests.get(settings.API_URL+"/bus_home2/")
        ad2 = requests.get(settings.API_URL+"/bus_home3/")
        ad3 = requests.get(settings.API_URL+"/bus_home4/")
        ad4 = requests.get(settings.API_URL+"/bus_home5/")
        ad5 = requests.get(settings.API_URL+"/bus_home6/")
        ad_cancel = requests.get(settings.API_URL+"/bus_cancel/")
        
        
        res6 = ad1.json()
        res20 = ad2.json()
        res15 = ad3.json()
        res16 = ad4.json()
        res17 = ad5.json()
        res_cancel=ad_cancel.json()
        return render(request, "bus_templates/trendcard2.html", {'res6': res6, 'res20': res20, 'res15': res15, 'res16': res16, 'res17': res17, 'res_cancel': res_cancel})


class bus3api(generics.ListCreateAPIView):
    queryset=bus_go_image2.objects.all()
    serializer_class=bus_go_image2_serialization

class bus_update3(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_go_image2.objects.all()
    serializer_class=bus_go_image2_serialization

class bus4api(generics.ListCreateAPIView):
    queryset=bus_go_container2.objects.all()
    serializer_class=bus_go_container2_serialization

class bus_update4(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_go_container2.objects.all()
    serializer_class=bus_go_container2_serialization

class bus5api(generics.ListCreateAPIView):
    queryset=bus_go_benefits2.objects.all()
    serializer_class=bus_go_benefits2_serialization

class bus_update5(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_go_benefits2.objects.all()
    serializer_class=bus_go_benefits2_serialization

class bus6api(generics.ListCreateAPIView):
    queryset=bus_go_terms2.objects.all()
    serializer_class=bus_go_terms2_serialization

class bus_update6(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_go_terms2.objects.all()
    serializer_class=bus_go_terms2_serialization



class bus_go_cancel_ins(generics.ListCreateAPIView):
    queryset=bus_go_cancel.objects.all()
    serializer_class=bus_go_cancel_serialization

class bus_go_cancel_upd(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_go_cancel.objects.all()
    serializer_class=bus_go_cancel_serialization

##################   card3    ##################

class bus7api(generics.ListCreateAPIView):
    queryset=bus_festival3.objects.all()
    serializer_class=bus_festival3_serialization
class bus_update7(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_festival3.objects.all()
    serializer_class=bus_festival3_serialization

def bus_main3(request):
    if request.method=="GET":
        ad=requests.get(settings.API_URL+"/bus_home7/")
        res4=ad.json()
        return render(request,"bus_templates/trendcard3.html",{'res4':res4})


##############   card4  ###################

class bus8api(generics.ListCreateAPIView):
    queryset=bus_special_code4.objects.all()
    serializer_class=bus_special_code4_serialization

class bus_update8(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_special_code4.objects.all()
    serializer_class=bus_special_code4_serialization


class bus9api(generics.ListCreateAPIView):
    queryset=bus_special_avail4.objects.all()
    serializer_class=bus_special_avail4_serialization

class bus_update9(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_special_avail4.objects.all()
    serializer_class=bus_special_avail4_serialization


class bus10api(generics.ListCreateAPIView):
    queryset=bus_special_terms4.objects.all()
    serializer_class=bus_special_terms4_serialization

class bus_update10(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_special_terms4.objects.all()
    serializer_class=bus_special_terms4_serialization



def bus_main4(request):
    if request.method == "GET":
        ad1 = requests.get(settings.API_URL+"/bus_home8/")
        ad2 = requests.get(settings.API_URL+"/bus_home9/")
        ad3 = requests.get(settings.API_URL+"/bus_home10/")
        res8 = ad1.json()
        res9 = ad2.json()
        res10 = ad3.json() 
        return render(request, "bus_templates/trendcard4.html", {'res8': res8, 'res9': res9, 'res10': res10 })
    

#############  card5  #############3


class bus11api(generics.ListCreateAPIView):
    queryset=bus_firstbus_code5.objects.all()
    serializer_class=bus_firstbus_code5_serialization

class bus_update11(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_firstbus_code5.objects.all()
    serializer_class=bus_firstbus_code5_serialization


class bus13api(generics.ListCreateAPIView):
    queryset=bus_firstbus_get5.objects.all()
    serializer_class=bus_firstbus_get5_serialization

class bus_update13(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_firstbus_get5.objects.all()
    serializer_class=bus_firstbus_get5_serialization


class bus12api(generics.ListCreateAPIView):
    queryset=bus_firstbus_terms5.objects.all()
    serializer_class=bus_firstbus_terms5_serialization

class bus_update12(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_firstbus_terms5.objects.all()
    serializer_class=bus_firstbus_terms5_serialization


def bus_main5(request):
    if request.method == "GET":
        ad1 = requests.get(settings.API_URL+"/bus_home11/")
        ad2 = requests.get(settings.API_URL+"/bus_home12/")
        ad3 = requests.get(settings.API_URL+"/bus_home13/")
        res = ad1.json()
        res1 = ad2.json()
        res2 = ad3.json()
        return render(request, "bus_templates/trendcard5.html", {'res': res, 'res1': res1, 'res2': res2 })
    
############## card6  ##########

class bus14api(generics.ListCreateAPIView):
    queryset=bus_busday_terms6.objects.all()
    serializer_class=bus_busday_terms6_serialization

class bus_update14(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_busday_terms6.objects.all()
    serializer_class=bus_busday_terms6_serialization

class bus15api(generics.ListCreateAPIView):
    queryset=bus_busday_image6.objects.all()
    serializer_class=bus_busday_image6_serialization

class bus_update15(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_busday_image6.objects.all()
    serializer_class=bus_busday_image6_serialization



def bus_main6(request):
    if request.method == "GET":
        ad1 = requests.get(settings.API_URL+"/bus_home14/")
        ad2 = requests.get(settings.API_URL+"/bus_home15/")
        res = ad1.json()
        res1 = ad2.json()
        return render(request, "bus_templates/trendcard6.html", {'res': res, 'res1': res1 })
    

############ card7 ############
    
class bus18api(generics.ListCreateAPIView):
    queryset=bus_easeday7.objects.all()
    serializer_class=bus_easeday7_serialization

class bus_update18(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_easeday7.objects.all()
    serializer_class=bus_easeday7_serialization

def bus_main8(request):
    if request.method=="GET":
        ad=requests.get(settings.API_URL+"/bus_home18/")
        res7=ad.json()
        return render(request,"bus_templates/trendcard7.html",{'res7':res7})



########## card8 #############

class bus19api(generics.ListCreateAPIView):
    queryset=bus_weekday8.objects.all()
    serializer_class=bus_weekday8_serialization

class bus_update19(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_weekday8.objects.all()
    serializer_class=bus_weekday8_serialization
def bus_main9(request):
    if request.method=="GET":
        ad=requests.get(settings.API_URL+"/bus_home19/")
        res8=ad.json()
        return render(request,"bus_templates/trendcard8.html",{'res8':res8})




################# card9 ################

class bus21api(generics.ListCreateAPIView):
    queryset=bus_icici11.objects.all()
    serializer_class=bus_icici11_serialization
    

class bus_update21(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_icici11.objects.all()
    serializer_class=bus_icici11_serialization
    

def bus_main11(request):
    if request.method=="GET":
        ad=requests.get(settings.API_URL+"/bus_home21/")
        res9=ad.json()
        return render(request,"bus_templates/trendcard9.html",{'res9':res9})
    



##########  card10 ###########


class bus20api(generics.ListCreateAPIView):
    queryset=bus_fest10.objects.all()
    serializer_class=bus_fest10_serialization

class bus_update20(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_fest10.objects.all()
    serializer_class=bus_fest10_serialization

def bus_main13(request):
    if request.method=="GET":
        ad=requests.get(settings.API_URL+"/bus_home20/")
        res12=ad.json()
        return render(request,"bus_templates/trendcard10.html",{'res12':res12})



########### card11 ###########
    
class bus22api(generics.ListCreateAPIView):
    queryset=bus_offer9.objects.all()
    serializer_class=bus_offer9_serialization
    

class bus_update22(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_offer9.objects.all()
    serializer_class=bus_offer9_serialization
    

def bus_main14(request):
    if request.method=="GET":
        ad=requests.get(settings.API_URL+"/bus_home22/")
        res13=ad.json()
        return render(request,"bus_templates/trendcard11.html",{'res13':res13})




########### card12 ###########
    
class bus23api(generics.ListCreateAPIView):
    queryset=bus_holiday12.objects.all()
    serializer_class=bus_holiday12_serialization

class bus_update23(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_holiday12.objects.all()
    serializer_class=bus_holiday12_serialization
def bus_main15(request):
    if request.method=="GET":
        ad=requests.get(settings.API_URL+"/bus_home23/")
        res15=ad.json()
        return render(request,"bus_templates/trendcard12.html",{'res15':res15})
    

########### card13 ###########
    
class bus24api(generics.ListCreateAPIView):
    queryset=bus_ride13.objects.all()
    serializer_class=bus_ride13_serialization

class bus_update24(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_ride13.objects.all()
    serializer_class=bus_ride13_serialization

def bus_main7(request):
    if request.method=="GET":
        ad=requests.get(settings.API_URL+"/bus_home24/")
        res7=ad.json()
        return render(request,"bus_templates/trendcard13.html",{'res7':res7})
    

#############  Bus search form  ############


class Busformapi(generics.ListCreateAPIView):
    queryset=bus_searchform.objects.all()
    serializer_class=bus_searchform_serialization

class Busformupdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=bus_searchform.objects.all()
    serializer_class=bus_searchform_serialization



def BusSearchForm(request):
    if request.method=="GET":
        ad=requests.get(settings.API_URL+"/Bus/")
        res=ad.json()
    return render(request,"bus_templates/search.html",{'res':res})



