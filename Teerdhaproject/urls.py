"""
URL configuration for Teerdhaproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from booking import views,hotel_views,flight_views,bus_views,cab_views
from django.urls import path, include
from django.contrib.auth import views as auth_views





urlpatterns = [

    path('admin/', admin.site.urls),
    path('teerdha_page',views.teerdha_page),


    # path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

   
    path('calculate-fare/',views.TaxiFareAPIView.as_view(), name='calculate_fare'),
    path('add_navigation_list/',views.add_navigation_list.as_view(),name="add_navigation_list"),
    path('Table_navigation_list/',views.Table_navigation_list.as_view(),name="Table_navigation_list"),
    path('Navigationlist/',views.Navigationlist.as_view(),name="Navigationlist"),
    path('Update_navigation_list/<int:pk>',views.Update_navigation_list.as_view(),name="Update_navigation_list"),
    path('Remove_navigation_list/<int:pk>',views.Remove_navigation_list.as_view(),name="Remove_navigation_list"),
    path('add_carousel_list/',views.add_carousel_list.as_view(),name="add_carousel_list"),
    path('Table_carousel_list/',views.Table_carousel_list.as_view(),name="Table_carousel_list"),
    path('Carousel_list/',views.Carousel_list.as_view(),name="Carousel_list"),
    path('Update_carousel_list/<int:pk>',views.Update_carousel_list.as_view(),name="Update_carousel_list"),
    path('Remove_carousel_list/<int:pk>',views.Remove_carousel_list.as_view(),name="Remove_carousel_list"),
    path('Carousel_home/',views.Carousel_home,name="Carousel_home"),
    # path('bus_form/',bus_views.bus_form,name="bus_form"),
    path('footer/',views.footer,name="footer"),



##################     flight ####################################################



    path('flight_home/',flight_views.flightsapi.as_view()),
    path('flight_update/<int:pk>/',flight_views.flight_update.as_view()),
    path('',flight_views.flights),

    # path('',include(router.urls)),

    ## kotak_offercard ##

    path('kotak_api/',flight_views.kotak_api.as_view()),
    path('kotak_update/<int:pk>/',flight_views.kotak_update.as_view()),

    path('kotak_api1/',flight_views.kotak_api1.as_view()),
    path('kotak_update1/<int:pk>/',flight_views.kotak_update1.as_view()),

    
    path('kotakterms_api/',flight_views.kotakterms_api.as_view()),
    path('kotakterms_update/<int:pk>/',flight_views.kotakterms_update.as_view()),

    path('kotakpolicy_api/',flight_views.kotakpolicy_api.as_view()),
    path('kotakpolicy_update/<int:pk>/',flight_views.kotakpolicy_update.as_view()),

    path('kotakpolicy_api1/',flight_views.kotakpolicy_api1.as_view()),
    path('kotakpolicy_update1/<int:pk>/',flight_views.kotakpolicy_update1.as_view()),
    path('kotak/',flight_views.kotak),

## first booking ##

    path('flight_offerfirst_lc/',flight_views.flight_offerfirst_lc.as_view()),
    path('flight_offerfirst_rud/<int:pk>/',flight_views.flight_offerfirst_rud.as_view()),
    path('flight_offerfirst1_lc/',flight_views.flight_offerfirst1_lc.as_view()),
    path('flight_offerfirst1_rud/<int:pk>/',flight_views.flight_offerfirst1_rud.as_view()),
    path('flight_offer_1/',flight_views.flight_offer_1),

#.........FAQ.........#
    
    path('faq_form/',flight_views.faq_form, name='faq_form'),
    path('flight_faqpage',flight_views.flight_faqpage),
    
    path('faq_home/',flight_views.faq_home),
    path('faq_del/<int:id>',flight_views.faq_del,name="faq_del"),
    path('faq_update/<int:id>',flight_views.faq_update,name="faq_update"),
    path('faq_edit/<int:id>',flight_views.faq_edit,name="faq_edit"),
    

# ..............yes_bank_offercard1...............
    path('card1_offerapi/',flight_views.card1_offerapi.as_view(),name="card1_offerapi"),
    path('card1_offerup/<int:pk>/',flight_views.card1_offerup.as_view(),name="card1_offerup"),
   
    path('card1_offerdetailesapi/',flight_views.card1_offerdetailesapi.as_view(),name="card1_offerdetailesapi"),
    path('card1_offerdetailes_up/<int:pk>/',flight_views.card1_offerdetailes_up.as_view(),name="card1_offerdetailes_up"),

    path('card1_offer_termsapi/',flight_views.card1_offer_termsapi.as_view(),name="card1_offer_termsapi"),
    path('card1_offerterms_up/<int:pk>/',flight_views.card1_offerterms_up.as_view(),name="card1_offerterms_up"),

    path('yes_bank_offercard/',flight_views.yes_bank_offercard),

#....refund....#
    path('zc_offerapi/',flight_views.zc_offerapi.as_view(),name="zc_offerapi"),
    path('zc_offer_update/<int:pk>/',flight_views.zc_offer_update.as_view(),name="zc_offer_update"),

    path('zc_termsapi/',flight_views.zc_termsapi.as_view(),name="zc_termsapi"),
    path('zc_terms_update/<int:pk>/',flight_views.zc_terms_update.as_view(),name="zc_terms_update"),
    
    path('zerocancellation/',flight_views.zerocancellation),

#...why choose us....#

    path('why_choose_lc/',flight_views.why_choose_lc.as_view()),
    path('why_choose_rud/<int:pk>/',flight_views.why_choose_rud.as_view()),
    # path('why_choose_us/',flight_views.why_choose_us),

#....question...#

    path('WhyChoose_ins/',flight_views.WhyChoose_ins),
    path('WhyChoose_flight/',flight_views.WhyChoose_flight),
    path('WhyChoose_update/<int:id>',flight_views.WhyChoose_update,name='WhyChoose_update'),
    path('WhyChoose_del/<int:id>',flight_views.WhyChoose_del,name='WhyChoose_del'),
    path('WhyChoose_edit/<int:id>',flight_views.WhyChoose_edit,name='WhyChoose_edit'),
    path('WhyChoose_home',flight_views.WhyChoose_home),

#.... icic....#

    path('icic_offerapi/',flight_views.icic_offerapi.as_view(),name="icic_offerapi"),
    path('icic_termsapi/',flight_views.icic_termsapi.as_view(),name="icic_termsapi"),

    path('icic_offer_update/<int:pk>',flight_views.icic_offer_update.as_view(),name="icic_offer_update"),
    path('icic_terms_update/<int:pk>',flight_views.icic_terms_update.as_view(),name="icic_terms_update"),
    
    path('icic/',flight_views.icic),

#...Sbi_offer....#

    path('sbiimageapi/',flight_views.sbiimageapi.as_view(),name="sbiimageapi"),
    path('sbiofferapi/',flight_views.sbiofferapi.as_view(),name="sbiofferapi"),
    path('sbitermsapi/',flight_views.sbitermsapi.as_view(),name="sbitermsapi"),


    path('sbiimage_up/<int:pk>/',flight_views.sbiimage_up.as_view(),name="sbiimage_up"),
    path('sbioffer_up/<int:pk>/',flight_views.sbioffer_up.as_view(),name="sbioffer_up"),
    path('sbiterms_up/<int:pk>/',flight_views. sbiterms_up.as_view(),name="sbiterms_up"),
    
    path('sbi/',flight_views.sbi),    

#########     HDFC      ################
    path('hdfc_logo_lc/',flight_views.hdfc_logo_lc.as_view()),
    path('hdfc_logo_rud/<int:pk>',flight_views.hdfc_logo_rud.as_view()),
    path('hdfc_offer_lc/',flight_views.hdfc_offer_lc.as_view()),
    path('hdfc_offer_rud/<int:pk>',flight_views.hdfc_offer_rud.as_view()),
    path('hdfc_offer_card/',flight_views.hdfc_offer_card),

    path('axis/',flight_views.axis,name="axis"),

## ............... AxiS Offer ...................#####

    path('axis_offerapi/',flight_views.axis_offerapi.as_view(),name="axis_offerapi"),
    path('axis_termsapi/',flight_views.axis_termsapi.as_view(),name="axis_termsapi"),

    
    path('axis_offer_update/<int:pk>',flight_views.axis_offer_update.as_view(),name="axis_offer_update"),
    path('axis_terms_update/<int:pk>',flight_views.axis_terms_update.as_view(),name="axis_terms_update"),
    
    
##....................HOTELS.............##

    path('hotelform/',hotel_views.hotelform,name="hotelform"),
    path('cardsapi/',hotel_views.cardsapi.as_view(),name='cardsapi'),
    path('cardsapi2/<int:pk>/',hotel_views.cardsapi2.as_view(),name='cardsapi2'),

    #...Hotel_quary..#

    path('hotel_cardsreg/',hotel_views.hotel_cardsreg),
    path('hotel_cardstb/',hotel_views.hotel_cardstb),
    path('hotel_cardsup/<int:id>',hotel_views.hotel_cardsup,name="hotel_cardsup"),
    path('hotel_cardsedit/<int:id>',hotel_views.hotel_cardsedit,name="hotel_cardsedit"),
    path('hotel_cardsdelete/<int:id>',hotel_views.hotel_cardsdelete,name="hotel_cardsdelete"),

    path('hotel_faqreg/',hotel_views.hotel_faqreg),
    # path('hotel_faqtab/',hotel_views.hotel_faqtab),
    path('hotel_faqupdate/<int:id>',hotel_views.hotel_faqupdate,name="hotel_faqupdate"),
    path('hotel_faqedit/<int:id>',hotel_views.hotel_faqedit,name="hotel_faqedit"),
    path('hotel_faqdelete/<int:id>',hotel_views.hotel_faqdelete,name="hotel_faqdelete"),
    
    #...HOtel_Axis...#

    path('hotel_axisform/',hotel_views.hotel_axisform,name="hotel_axisform"),
    path('axis_api/',hotel_views.axis_api.as_view(),name='axis_api'),
    path('axis_update/<int:pk>/',hotel_views.axis_update.as_view(),name='axis_update'),
    path('axis_api1/',hotel_views.axis_api1.as_view(),name='axis_api1'),
    path('aixs_update1/<int:pk>/',hotel_views.aixs_update1.as_view(),name='aixs_update1'),
    path('axispolicy_api/',hotel_views.axispolicy_api.as_view(),name='axispolicy_api'),
    path('axispolicy_update/<int:pk>/',hotel_views.axispolicy_update.as_view(),name='axispolicy_update'),

    #....Hotel_icici...#
    
    path('hotel_iciciform/',hotel_views.hotel_iciciform,name="hotel_iciciform"),
    path('icici_api/',hotel_views.icici_api.as_view(),name='icici_api'),
    path('icici_update/<int:pk>/',hotel_views.icici_update.as_view(),name='icici_update'),
    path('icici_api1/',hotel_views.icici_api1.as_view(),name='icici_api1'),
    path('icici_update1/<int:pk>/',hotel_views.icici_update1.as_view(),name='icici_update1'),
    path('icicipolicy_api/',hotel_views.icicipolicy_api.as_view(),name='icicipolicy_api'),
    path('icicipolicy_update/<int:pk>/',hotel_views.icicipolicy_update.as_view(),name='icicipolicy_update'),

    #...Hotel_HSBC...#

    path('hotel_hsbcform/',hotel_views.hotel_hsbcform,name="hotel_hsbcform"),
    path('hsbc_api/',hotel_views.hsbc_api.as_view(),name='hsbc_api'),
    path('hsbc_update/<int:pk>/',hotel_views.hsbc_update.as_view(),name='hsbc_update'),
    path('hsbc_api1/',hotel_views.hsbc_api1.as_view(),name='hsbc_api1'),
    path('hsbc_update1/<int:pk>/',hotel_views.hsbc_update1.as_view(),name='hsbc_update1'),
    path('hsbcpolicy_api/',hotel_views.hsbcpolicy_api.as_view(),name='hsbcpolicy_api'),
    path('hsbcpolicy_update/<int:pk>/',hotel_views.hsbcpolicy_update.as_view(),name='hsbcpolicy_update'),

    #...Hotel_SBI...#

    path('hotel_sbiform/',hotel_views.hotel_sbiform,name="hotel_sbiform"),
    path('sbi_api/',hotel_views.sbi_api.as_view(),name='sbi_api'),
    path('sbi_update/<int:pk>/',hotel_views.sbi_update.as_view(),name='sbi_update'),
    path('sbi_api1/',hotel_views.sbi_api1.as_view(),name='sbi_api1'),
    path('sbi_update1/<int:pk>/',hotel_views.sbi_update1.as_view(),name='sbi_update1'),
    path('sbipolicy_api/',hotel_views.sbipolicy_api.as_view(),name='sbipolicy_api'),
    path('sbipolicy_update/<int:pk>/',hotel_views.sbipolicy_update.as_view(),name='sbipolicy_update'),

    #...Hotel_KOTAK...#

    path('hotel_kotakform/',hotel_views.hotel_kotakform,name="hotel_kotakform"),
    path('hotel_kotakapi/',hotel_views.hotel_kotakapi.as_view(),name='hotel_kotakapi'),
    path('hotel_kotakupdate/<int:pk>/',hotel_views.hotel_kotakupdate.as_view(),name='hotel_kotakupdate'),
    path('hotel_kotakapi1/',hotel_views.hotel_kotakapi1.as_view(),name='hotel_kotakapi1'),
    path('hotel_kotakupdate1/<int:pk>/',hotel_views.hotel_kotakupdate1.as_view(),name='hotel_kotakupdate1'),
    path('hotel_kotakpolicyapi/',hotel_views.hotel_kotakpolicyapi.as_view(),name='hotel_kotakpolicyapi'),
    path('hotel_kotakpolicyupdate/<int:pk>/',hotel_views.hotel_kotakpolicyupdate.as_view(),name='hotel_kotakpolicyupdate'),

    #.....BOB.....#

    path('hotel_bobform/',hotel_views.hotel_bobform,name="hotel_bobform"),
    path('hotel_bobapi/',hotel_views.hotel_bobapi.as_view(),name='hotel_bobapi'),
    path('hotel_bobupdate/<int:pk>/',hotel_views.hotel_bobupdate.as_view(),name='hotel_bobupdate'),
    path('hotel_bobapi1/',hotel_views.hotel_bobapi1.as_view(),name='hotel_bobapi1'),
    path('hotel_bobupdate1/<int:pk>/',hotel_views.hotel_bobupdate1.as_view(),name='hotel_bobupdate1'),
    path('hotel_bobpolicyapi/',hotel_views.hotel_bobpolicyapi.as_view(),name='hotel_bobpolicyapi'),
    path('hotel_bobpolicyupdate/<int:pk>/',hotel_views.hotel_bobpolicyupdate.as_view(),name='hotel_bobpolicyupdate'),


    #...Hotel_FEDERAL...#

    path('hotel_federalform/',hotel_views.hotel_federalform,name="hotel_federalform"),
    path('federal_api/',hotel_views.federal_api.as_view(),name='federal_api'),
    path('federal_update/<int:pk>/',hotel_views.federal_update.as_view(),name='federal_update'),
    path('federal_api1/',hotel_views.federal_api1.as_view(),name='federal_api1'),
    path('federal_update1/<int:pk>/',hotel_views.federal_update1.as_view(),name='federal_update1'),
    path('federalpolicy_api/',hotel_views.federalpolicy_api.as_view(),name='federalpolicy_api'),
    path('federalpolicy_update/<int:pk>/',hotel_views.federalpolicy_update.as_view(),name='federalpolicy_update'),


    ############# cab's search form ############# 

    path('cab',cab_views.cab,name='cab'),
    ###############  offers on cab cards #############
    path('cab_insert/',cab_views.cabsapi.as_view()),
    path('cab_update/<int:pk>/',cab_views.cab_update.as_view()),
    path('cab_main/',cab_views.cab_main),

    ######## 2nd page for 1st  card ##############

    path('festive_insert/',cab_views.cabcard1.as_view()),
    path('festive_update/<int:pk>/',cab_views.festive_update.as_view()),
    path('festive_main/',cab_views.festive_main),
     ######## 2nd page for  2nd card ##############

    path('rental_insert/',cab_views.cabcard2.as_view()),
    path('rental_update/<int:pk>/',cab_views.rental_update.as_view()),
    path('rental_main/',cab_views.rental_main),
     ######## 2nd page for  3rd card ##############

    path('anytime_insert/',cab_views.cabcard3.as_view()),
    path('anytime_update/<int:pk>/',cab_views.anytime_update.as_view()),
    path('anytime_main/',cab_views.anytime_main),

     ######## 2nd page for  4th card ##############

    path('ride_insert/',cab_views.cabcard4.as_view()),
    path('ride_update/<int:pk>/',cab_views.ride_update.as_view()),
    path('ride_main/',cab_views.ride_main),
    
     ######## 2nd page for  5th card ##############

    path('familyfun_insert/',cab_views.cabcard5.as_view()),
    path('familyfun_update/<int:pk>/',cab_views.familyfun_update.as_view()),
    path('familyfun_main/',cab_views.familyfun_main),

 ######## 2nd page for  6th card ##############

    path('easy_insert/',cab_views.cabcard6.as_view()),
    path('easy_update/<int:pk>/',cab_views.easy_update.as_view()),
    path('easy_main/',cab_views.easy_main),


 ######## 2nd page for  7th card ##############

    path('offer15_insert/',cab_views.cabcard7.as_view()),
    path('offer15_update/<int:pk>/',cab_views.offer15_update.as_view()),
    path('offer15_main/',cab_views.offer15_main),


 ######## 2nd page for  8th card ##############

    path('paytm_card_insert/',cab_views.cabcard8.as_view()),
    path('paytm_card_update/<int:pk>/',cab_views.paytm_card_update.as_view()),
    path('paytm_card_main/',cab_views.paytm_card_main),
    
####   Django- Why Choose us ####
    path('WhyChoose/',cab_views.WhyChoose),
    path('WhyChoosecard/',cab_views.WhyChoosecard),
    path('WhyChoose_crud_update/<int:id>',cab_views.WhyChoose_crud_update,name='WhyChoose_crud_update'),
    path('WhyChoose_crud_del/<int:id>',cab_views.WhyChoose_crud_del,name='WhyChoose_crud_del'),
    path('WhyChoose_crud_edit/<int:id>',cab_views.WhyChoose_crud_edit,name='WhyChoose_crud_edit'),
    path('cabs_whychoose',cab_views.cabs_whychoose, name='cabs_whychoose'),
    

    #############  cab faq ############

    path('cabfaq_upd/',cab_views.cabfaq_upd,name='cabfaq_upd'),
    path('cabfaq_crud_update/<int:id>',cab_views.cabfaq_crud_update,name='cabfaq_crud_update'),
    path('cabfaq_crud_del/<int:id>',cab_views.cabfaq_crud_del,name='cabfaq_crud_del'),
    path('cabfaq_crud_edit/<int:id>',cab_views.cabfaq_crud_edit,name='cabfaq_crud_edit'),
    path('cabfaq_home/',cab_views.cabfaq_home),

   ######....BUSES....#####

    path('bus_home/',bus_views.busapi.as_view()),
    path('bus_update/<int:pk>/',bus_views.bus_update.as_view()),
    path('bus_main/',bus_views.bus_main),
    path('bus_whychoose_form/',bus_views.bus_whychoose_form),
    path('bus_faq_form/',bus_views.bus_faq_form),
    path('bus_whychoose_content/',bus_views.bus_whychoose_content),
    path('bus_faq_content/',bus_views.bus_faq_content),
    path('bus_whychoose_op/',bus_views.bus_whychoose_op, name='bus_whychoose_op'),
    path('bus_faq_op/',bus_views.bus_faq_op, name='bus_faq_op'),



    path('bus_whychoose_delete/<int:id>',bus_views.bus_whychoose_delete,name="bus_whychoose_delete"),
    path('bus_whychoose_update/<int:id>',bus_views.bus_whychoose_update,name="bus_whychoose_update"),
    path('bus_whychoose_edit/<int:id>',bus_views.bus_whychoose_edit,name="bus_whychoose_edit"),


    path('bus_faq_delete/<int:id>',bus_views.bus_faq_delete,name="bus_faq_delete"),
    path('bus_faq_update/<int:id>',bus_views.bus_faq_update,name="bus_faq_update"),
    path('bus_faq_edit/<int:id>',bus_views.bus_faq_edit,name="bus_faq_edit"),



    path('bus_whychoose_upd/<int:id>',bus_views.bus_whychoose_upd,name="bus_whychoose_upd"),
    path('bus_faq_upd/',bus_views.bus_faq_upd),
    


    path('bus_home1/',bus_views.bus1api.as_view()),
    path('bus_update1/<int:pk>/',bus_views.bus_update1.as_view()),
    path('bus_home01/',bus_views.bus0api.as_view()),
    path('bus_update0/<int:pk>/',bus_views.bus_update0.as_view()),
    path('bus_main1/',bus_views.bus_main1),


    path('bus_home2/',bus_views.bus2api.as_view()),
    path('bus_update2/<int:pk>/',bus_views.bus_update2.as_view()),
    path('bus_main2/',bus_views.bus_main2),

    path('bus_home3/',bus_views.bus3api.as_view()),
    path('bus_update3/<int:pk>/',bus_views.bus_update3.as_view()),


    path('bus_home4/',bus_views.bus4api.as_view()),
    path('bus_update4/<int:pk>/',bus_views.bus_update4.as_view()),

    path('bus_home5/',bus_views.bus5api.as_view()),
    path('bus_update5/<int:pk>/',bus_views.bus_update5.as_view()),


    path('bus_home6/',bus_views.bus6api.as_view()),
    path('bus_update6/<int:pk>/',bus_views.bus_update6.as_view()),


    path('bus_cancel/',bus_views.bus_go_cancel_ins.as_view()),
    path('bus_go_cancel_upd/<int:pk>/',bus_views.bus_go_cancel_upd.as_view()),


    path('bus_home7/',bus_views.bus7api.as_view()),
    path('bus_update7/<int:pk>/',bus_views.bus_update7.as_view()),
    path('bus_main3/',bus_views.bus_main3),


    path('bus_home8/',bus_views.bus8api.as_view()),
    path('bus_update8/<int:pk>/',bus_views.bus_update8.as_view()),
    path('bus_main4/',bus_views.bus_main4),

    path('bus_home9/',bus_views.bus9api.as_view()),
    path('bus_update9/<int:pk>/',bus_views.bus_update9.as_view()),
    

    path('bus_home10/',bus_views.bus10api.as_view()),
    path('bus_update10/<int:pk>/',bus_views.bus_update10.as_view()),



    path('bus_home11/',bus_views.bus11api.as_view()),
    path('bus_update11/<int:pk>/',bus_views.bus_update11.as_view()),


    path('bus_home12/',bus_views.bus12api.as_view()),
    path('bus_update12/<int:pk>/',bus_views.bus_update12.as_view()),
    

    path('bus_home13/',bus_views.bus13api.as_view()),
    path('bus_update13/<int:pk>/',bus_views.bus_update13.as_view()),
    path('bus_main5/',bus_views.bus_main5),


    path('bus_home14/',bus_views.bus14api.as_view()),
    path('bus_update14/<int:pk>/',bus_views.bus_update14.as_view()),
    

    path('bus_home15/',bus_views.bus15api.as_view()),
    path('bus_update15/<int:pk>/',bus_views.bus_update15.as_view()),
    path('bus_main6/',bus_views.bus_main6),


    path('bus_home18/',bus_views.bus18api.as_view()),
    path('bus_update18/<int:pk>/',bus_views.bus_update18.as_view()),
    path('bus_main8/',bus_views.bus_main8),


    path('bus_home19/',bus_views.bus19api.as_view()),
    path('bus_update19/<int:pk>/',bus_views.bus_update19.as_view()),
    path('bus_main9/',bus_views.bus_main9),


    path('bus_home20/',bus_views.bus20api.as_view()),
    path('bus_update20/<int:pk>/',bus_views.bus_update20.as_view()),
    path('bus_main13/',bus_views.bus_main13),


    path('bus_home21/',bus_views.bus21api.as_view()),
    path('bus_update21/<int:pk>/',bus_views.bus_update21.as_view()),
    path('bus_main14/',bus_views.bus_main14),


    path('bus_home22/',bus_views.bus22api.as_view()),
    path('bus_update22/<int:pk>/',bus_views.bus_update22.as_view()),
    path('bus_main11/',bus_views.bus_main11),


    path('bus_home23/',bus_views.bus23api.as_view()),
    path('bus_update23/<int:pk>/',bus_views.bus_update23.as_view()),
    path('bus_main15/',bus_views.bus_main15),


    path('bus_home24/',bus_views.bus24api.as_view()),
    path('bus_update24/<int:pk>/',bus_views.bus_update24.as_view()),
    path('bus_main7/',bus_views.bus_main7),



    path('navbar_page/',views.navbar_page),
    path('navbar_table/',views.navbar_table),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('hotel_faqtab/',hotel_views.hotel_faqtab, name='hotel_faqtab'),


    #....Dashboard....#

    path('flightoffers_insertform/',views.flightoffers_insertform,name="flightoffers_insertform"),
    path('flight_offertb/',views.flight_offertb,name="flight_offertb"),
    path('busoffers_insertform/',views.busoffers_insertform,name="busoffers_insertform"),
    path('buses_offertb/',views.buses_offertb,name="buses_offertb"),
    path('hoteloffers_insertform/',views.hoteloffers_insertform,name="hoteloffers_insertform"),
    path('hotels_offertb/',views.hotels_offertb,name="hotels_offertb"),


    path('dashboard/',views.dashboard,name='dashboard'),
    path('login/', views.login_view, name='login'), 
    path('logout/', views.logout_view, name='logout'),
    path('authenticate/', views.login_view, name='authenticate'),

    # path('admin_insertform/', views.admin_insertform, name='admin_insertform'),
    # path('sidebar_with_nav/', views.sidebar_with_nav, name='sidebar_with_nav'),


     ############## cabs Dashboard ####
    path('cabs_insert_dashboard/',views.cabs_insert_dashboard,name="cabs_insert_dashboard"),
    path('cabs_table_dashboard/',views.cabs_table_dashboard,name="cabs_table_dashboard"),

    path('cabs_insert_2ndpagedb/',views.cabs_insert_2ndpagedb,name="cabs_insert_2ndpagedb"),
    path('cabs_table_2ndpagedb/',views.cabs_table_2ndpagedb,name="cabs_table_2ndpagedb"),

     ############## Buses Dashboard ####

    path('buses2ndpage_insertform/',views.buses2ndpage_insertform,name="buses2ndpage_insertform"),
    path('bus_2ndpages/',views.bus_2ndpages,name="bus_2ndpages"),


    path('flight2ndpage_insertform/',views.flight2ndpage_insertform,name="flight2ndpage_insertform"),
    path('flight_2ndpages/',views.flight_2ndpages,name="flight_2ndpages"),
    path('flight2ndpage_updateform/',views.flight2ndpage_updateform,name="flight2ndpage_updateform"),
    path('flight_2ndpagesupdate/',views.flight_2ndpagesupdate,name="flight_2ndpagesupdate"),
    path('hotel2ndpage_insertform/',views.hotel2ndpage_insertform,name="hotel2ndpage_insertform"),
    path('hotel_2ndpages/',views.hotel_2ndpages,name="hotel_2ndpages"),


    path('admin_insertforms/',views.admin_insertforms),
    path("sidebar_retrieve/",views.sidebar_retrieve),
    path("airports/",views.airports,name='airports'),

    path('password_reset_view/',views.password_reset_view,name="password_reset_view"),
    path('update_profile/',views.update_profile,name="update_profile"),
    path('ajax_test/', views.ajax_test, name='ajax_test')
    


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
