from django.shortcuts import render,redirect
from .models import *
from .serialization import flights_serialization,kotak_serialization,kotak_serialization1,kotakterms_serialization,kotakpolicy_serialization,kotakpolicy1_serialization
from rest_framework import generics
import requests
from .serialization import *
from django.http import HttpResponse
from django.conf import settings


class flightsapi(generics.ListCreateAPIView):
    queryset=flights_offercards.objects.all()
    serializer_class=flights_serialization

class flight_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=flights_offercards.objects.all()
    serializer_class=flights_serialization


##################### FAQS #############################

  
def faq_form(request):
    if request.method == "POST":
       
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        k3 = flightfaqs(question=question, answer=answer)
        k3.save()
        return HttpResponse("Record is inserted")
    return render(request,"flight_templates/flightfaq_ins.html")

def flight_faqpage(request):
    if request.method == "GET":
        k3 = flightfaqs.objects.all()
    return render(request,"flight_templates/faqs.html", {'k3': k3})

############  CRUD OPERATIONS FOR FAQS  #########################



def faq_update(request,id):
    if request.method == "POST":
       
        question = request.POST['question']
        answer = request.POST['answer']
        k3=flightfaqs.objects.get(id=id)
        k3.question=question
        k3.answer = answer
       
        k3.save()
      
        return redirect("/faq_home")
    return render(request,"flight_templates/flightfaq_up.html")

def  faq_del(request,id):
        k3=flightfaqs.objects.get(id=id)
        k3.delete()
        return redirect("/faq_home")

def faq_edit(request,id):
    if request.method=="GET":
        k3=flightfaqs.objects.get(id=id)
    return render(request,"flight_templates/flightfaq_up.html",{'k3':k3})


def faq_home(request):
    if request.method == "POST":
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        k3 = flightfaqs(question=question, answer=answer)
        k3.save()
        return redirect("/faq_home")


    if request.method == "GET":
        k3 = flightfaqs.objects.all()
        Sidebar=sidebar_dashboard.objects.all()
        nav_item=navbar.objects.all()
    return render(request,"flight_templates/flightfaq_table.html",{'k3': k3,'Sidebar':Sidebar, 'nav_item':nav_item})  


def flights(request):
    k =choosing_content.objects.all()     

    if request.method=="GET":
        nav=navbar.objects.all()
        ad=requests.get(settings.API_URL+"/flight_home/")
        res=ad.json()
        k3 = flightfaqs.objects.all()
        wc = requests.get(settings.API_URL+"/why_choose_lc/")
        wcu = wc.json()
        return render(request,"flight_templates/c.html",{'nav':nav,'res':res,'k3':k3,'wcu':wcu,'k':k})


class kotak_api(generics.ListCreateAPIView):
    queryset=flights_kotak_offer.objects.all()
    serializer_class=kotak_serialization

class kotak_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=flights_kotak_offer.objects.all()
    serializer_class=kotak_serialization

class kotak_api1(generics.ListCreateAPIView):
    queryset=flights_kotak_offer1.objects.all()
    serializer_class=kotak_serialization1

class kotak_update1(generics.RetrieveUpdateDestroyAPIView):
    queryset=flights_kotak_offer1.objects.all()
    serializer_class=kotak_serialization1

class kotakterms_api(generics.ListCreateAPIView):
    queryset=flights_kotak_terms.objects.all()
    serializer_class=kotakterms_serialization

class kotakterms_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=flights_kotak_terms.objects.all()
    serializer_class=kotakterms_serialization

class kotakpolicy_api(generics.ListCreateAPIView):
    queryset=flights_policy.objects.all()
    serializer_class=kotakpolicy_serialization

class kotakpolicy_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=flights_policy.objects.all()
    serializer_class=kotakpolicy_serialization

class kotakpolicy_api1(generics.ListCreateAPIView):
    queryset=flights_policy1.objects.all()
    serializer_class=kotakpolicy1_serialization

class kotakpolicy_update1(generics.RetrieveUpdateDestroyAPIView):
    queryset=flights_policy1.objects.all()
    serializer_class=kotakpolicy1_serialization    

def kotak(request):
    if request.method=="GET":
        sh=requests.get(settings.API_URL+"/kotak_api/")
        rdx=sh.json()
        sk=requests.get(settings.API_URL+"/kotak_api1/")
        rx=sk.json()
        sj=requests.get(settings.API_URL+"/kotakterms_api/")
        rs=sj.json()
        si=requests.get(settings.API_URL+"/kotakpolicy_api/")
        rd=si.json()
        sl=requests.get(settings.API_URL+"/kotakpolicy_api1/")
        rp=sl.json()
        
        return render(request,"flight_templates/kotak_offer.html",{'rdx':rdx,'rx':rx,'rs':rs,'rd':rd,'rp':rp})

## first booking ##
    

class flight_offerfirst_lc(generics.ListCreateAPIView):
    queryset=flight_offer_first.objects.all()
    serializer_class=flight_firstser
 
class flight_offerfirst_rud(generics.RetrieveUpdateDestroyAPIView):
    queryset=flight_offer_first.objects.all()
    serializer_class=flight_firstser

class flight_offerfirst1_lc(generics.ListCreateAPIView):
    queryset=flight_offer_first1.objects.all()
    serializer_class=flight_first1ser
 
class flight_offerfirst1_rud(generics.RetrieveUpdateDestroyAPIView):
    queryset=flight_offer_first1.objects.all()
    serializer_class=flight_first1ser


def flight_offer_1(request):
    if request.method == "GET":
        fo = requests.get(settings.API_URL+"/flight_offerfirst_lc/")
        flight = fo.json()
        fo1 = requests.get(settings.API_URL+"/flight_offerfirst1_lc/")
        flight_1 = fo1.json()
        return render(request,"flight_templates/flight_offer_1.html", {'flight': flight, 'flight_1': flight_1})


#.........................................Yes Bank  card1 start here.....................................
#.................card1_offer................
class card1_offerapi(generics.ListCreateAPIView):
    queryset=card1_offers.objects.all()
    serializer_class=card1_offers_serialization

class card1_offerup(generics.RetrieveUpdateDestroyAPIView):
    queryset=card1_offers.objects.all()
    serializer_class=card1_offers_serialization

#..................card1_offerdetailes.................

class card1_offerdetailesapi(generics.ListCreateAPIView):
    queryset=card1_offerdetailes.objects.all()
    serializer_class=card1_offerdetailes_serialization

class card1_offerdetailes_up(generics.RetrieveUpdateDestroyAPIView):
    queryset=card1_offerdetailes.objects.all()
    serializer_class=card1_offerdetailes_serialization

#....................card1_offer_terms & conditions..................

class card1_offer_termsapi(generics.ListCreateAPIView):
    queryset=card1_terms_conditions.objects.all()
    serializer_class=card1_terms_conditions_serialization

class card1_offerterms_up(generics.RetrieveUpdateDestroyAPIView):
    queryset=card1_terms_conditions.objects.all()
    serializer_class=card1_terms_conditions_serialization

#.................... To Retrieve the data...........................

def yes_bank_offercard(request):
    if request.method=="GET":
        co=requests.get(settings.API_URL+"/card1_offerapi/")
        res1=co.json()
        cod=requests.get(settings.API_URL+"/card1_offerdetailesapi/")
        res2=cod.json()
        cot=requests.get(settings.API_URL+"/card1_offer_termsapi/")
        res3=cot.json()
        return render(request,"flight_templates/yes_bank_offercard.html",{'res1':res1,'res2':res2,'res3':res3})

##........refundcards........##


class zc_offerapi(generics.ListCreateAPIView):
    queryset=Zero_cancellation_offer.objects.all()
    serializer_class=ZC_offer_serialization

class zc_offer_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=Zero_cancellation_offer.objects.all()
    serializer_class=ZC_offer_serialization



class zc_termsapi(generics.ListCreateAPIView):
    queryset=Zero_cancellation_terms.objects.all()
    serializer_class=zc_terms_serialization

class zc_terms_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=Zero_cancellation_terms.objects.all()
    serializer_class=zc_terms_serialization


def zerocancellation(request):
    if request.method=="GET":
        zco=requests.get(settings.API_URL+"/zc_offerapi/")
        res1=zco.json()
        zct=requests.get(settings.API_URL+"/zc_termsapi/")
        res2=zct.json()
        return render(request,"flight_templates/zero_offer.html",{'res1':res1,'res2':res2})  

#......why choose us...#
    
class why_choose_lc(generics.ListCreateAPIView):
    queryset=why_choose.objects.all()
    serializer_class=why_chooseser
 
class why_choose_rud(generics.RetrieveUpdateDestroyAPIView):
    queryset=why_choose.objects.all()
    serializer_class=why_chooseser

#....question...#
    
  
def WhyChoose_ins(request):
    if request.method == "POST":
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        k = choosing_content(question=question, answer=answer)
        k.save()
        return HttpResponse("Record is inserted")
    return render(request, "flight_templates/WhyChoose_insert.html")

def WhyChoose_flight(request):
    if request.method == "GET":
        k =choosing_content.objects.all()
    return render(request, "flight_templates/whychoose.html", {'k': k})

############ CRUD OPERATIONS FOR WHY CHOOSE US  #########################



def WhyChoose_update(request,id):
    if request.method == "POST":
        question = request.POST['question']
        answer = request.POST['answer']
        k=choosing_content.objects.get(id=id)
        k.question=question
        k.answer = answer
        k.save()
        return redirect("/WhyChoose_home")
    return render(request,"flight_templates/whychoose_update.html")

def  WhyChoose_del(request,id):
        k=choosing_content.objects.get(id=id)
        k.delete()
        return redirect("/WhyChoose_home")

def WhyChoose_edit(request,id):
    if request.method=="GET":
        k=choosing_content.objects.get(id=id)
    return render(request,"flight_templates/whychoose_update.html",{'k':k})

 

def WhyChoose_home(request):
    if request.method == "POST":
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        k = choosing_content(question=question, answer=answer)
        k.save()
        return redirect("/WhyChoose_home")
    
    if request.method == "GET":
        k = choosing_content.objects.all()
        Sidebar=sidebar_dashboard.objects.all()
        nav_item=navbar.objects.all()
    return render(request,"flight_templates/whychoose_table.html",{'k': k,'Sidebar':Sidebar, 'nav_item':nav_item})



#....icic....#

class icic_offerapi(generics.ListCreateAPIView):
    queryset=icic_offer.objects.all()
    serializer_class=icic_serialization

class icic_offer_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=icic_offer.objects.all()
    serializer_class=icic_serialization



class icic_termsapi(generics.ListCreateAPIView):
    queryset=icic_terms.objects.all()
    serializer_class=icici_serialization

class icic_terms_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=icic_terms.objects.all()
    serializer_class=icici_serialization


def icic(request):
    if request.method=="GET":
        zco=requests.get(settings.API_URL+"/icic_offerapi/")
        res1=zco.json()
        zct=requests.get(settings.API_URL+"/icic_termsapi/")
        res2=zct.json()
        return render(request,"flight_templates/icici.html",{'res1':res1,'res2':res2})        
    
from .models import sbiimage,sbioffer,sbiterms
from .serialization import sbiimage_serialization,sbioffer_serialization,sbiterms_serialization

class sbiimageapi(generics.ListCreateAPIView):
    queryset=sbiimage.objects.all()
    serializer_class=sbiimage_serialization

class sbiimage_up(generics.RetrieveUpdateDestroyAPIView):
    queryset=sbiimage.objects.all()
    serializer_class=sbiimage_serialization


class sbiofferapi(generics.ListCreateAPIView):
    queryset=sbioffer.objects.all()
    serializer_class=sbioffer_serialization

class sbioffer_up(generics.RetrieveUpdateDestroyAPIView):
    queryset=sbioffer.objects.all()
    serializer_class=sbioffer_serialization


class sbitermsapi(generics.ListCreateAPIView):
    queryset=sbiterms.objects.all()
    serializer_class=sbiterms_serialization

class sbiterms_up(generics.RetrieveUpdateDestroyAPIView):
    queryset=sbiterms.objects.all()
    serializer_class=sbiterms_serialization

def sbi(request):
    if request.method=="GET":
        si=requests.get(settings.API_URL+"/sbiimageapi/")
        res1=si.json()
        so=requests.get(settings.API_URL+"/sbiofferapi/")
        res2=so.json()
        st=requests.get(settings.API_URL+"/sbitermsapi/")
        res3=st.json()
        return render(request,"flight_templates/sbi.html",{'res1':res1,'res2':res2,'res3':res3})  

class hdfc_logo_lc(generics.ListCreateAPIView):
    queryset=hdfc_logo.objects.all()
    serializer_class=hdfc_logoser

class hdfc_logo_rud(generics.RetrieveUpdateDestroyAPIView):
    queryset=hdfc_logo.objects.all()
    serializer_class=hdfc_logoser  

class hdfc_offer_lc(generics.ListCreateAPIView):
    queryset=hdfc_offer.objects.all()
    serializer_class=hdfc_offerser

class hdfc_offer_rud(generics.RetrieveUpdateDestroyAPIView):
    queryset=hdfc_offer.objects.all()
    serializer_class=hdfc_offerser  

def hdfc_offer_card(request):
    if request.method=="GET":
        hl=hdfc_logo.objects.all()
        # hl=requests.get(settings.API_URL+"/hdfc_logo_lc/")
        # hdfc_logo=hl.json()
        h=hdfc_offer.objects.all()
        # h=requests.get(settings.API_URL+"/hdfc_offer_lc/")
        # hdfc=h.json()
        return render(request,"flight_templates/hdfc_offer_card.html",{'hdfc':h,'hdfc_logo':hl})  



# def flight_offers_card_page_2(request):
#     if request.method=="GET":
#         k=flight_offers7.objects.all()
#         k1=flight_offers8.objects.all()
#     return render(request,"flight_templates/flight_offers_card_page_2.html",{'k':k, 'k1':k1})



from .models import flight_offers7,flight_offers8
from .serialization import axis_offer_serialization,axis_terms_serialization


##........... Axis card 2nd page.............#

class axis_offerapi(generics.ListCreateAPIView):
    queryset=flight_offers7.objects.all()
    serializer_class=axis_offer_serialization

class axis_offer_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=flight_offers7.objects.all()
    serializer_class=axis_offer_serialization


class axis_termsapi(generics.ListCreateAPIView):
    queryset=flight_offers8.objects.all()
    serializer_class=axis_terms_serialization

class axis_terms_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=flight_offers8.objects.all()
    serializer_class=axis_terms_serialization

def axis(request):
    if request.method=="GET":
        ax=requests.get(settings.API_URL+"/axis_offerapi/")
        res1=ax.json()
        ao=requests.get(settings.API_URL+"/axis_termsapi/")
        res2=ao.json()
        return render(request,"flight_templates/flight_offers_card_page_2.html",{'res1':res1,'res2':res2})  

