from rest_framework import serializers
from .models import *
class TaxiFareSerializer(serializers.Serializer):
    dep_lat = serializers.FloatField()
    dep_lng = serializers.FloatField()
    arr_lat = serializers.FloatField()
    arr_lng = serializers.FloatField()


class Navigationdata(serializers.ModelSerializer):
    class Meta:
        model=Naviagtion_bar
        fields='__all__'
class Carouseldata(serializers.ModelSerializer):
    class Meta:
        model=Home_carousel
        fields='__all__'


########################  flights    ################################
        
from rest_framework import serializers
from .models import *

class flights_serialization(serializers.ModelSerializer):
    class Meta:
        model=flights_offercards
        fields="__all__"

class kotak_serialization(serializers.ModelSerializer):
    class Meta:
        model=flights_kotak_offer
        fields="__all__"

class kotakterms_serialization(serializers.ModelSerializer):
    class Meta:
        model=flights_kotak_terms
        fields="__all__" 

class kotakpolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=flights_policy
        fields="__all__" 

class kotakpolicy1_serialization(serializers.ModelSerializer):
    class Meta:
        model=flights_policy1
        fields="__all__"

class kotak_serialization1(serializers.ModelSerializer):
    class Meta:
        model=flights_kotak_offer1
        fields="__all__"        

## first booking ##

class flight_firstser(serializers.ModelSerializer):
    class Meta:
        model=flight_offer_first
        fields="__all__"

class flight_first1ser(serializers.ModelSerializer):
    class Meta:
        model=flight_offer_first1
        fields="__all__"


# ..................card1 serialization Yes Bank....................
class card1_offers_serialization(serializers.ModelSerializer):
    class Meta:
        model=card1_offers
        fields="__all__"

class card1_offerdetailes_serialization(serializers.ModelSerializer):
    class Meta:
        model=card1_offerdetailes
        fields="__all__"

class card1_terms_conditions_serialization(serializers.ModelSerializer):
    class Meta:
        model=card1_terms_conditions
        fields="__all__"

## FAQ ##
  
        
#................100% Refund card...........

from .models import  Zero_cancellation_offer,Zero_cancellation_terms

class ZC_offer_serialization(serializers.ModelSerializer):
    class Meta:
        model=Zero_cancellation_offer
        fields="__all__"

class zc_terms_serialization(serializers.ModelSerializer):
    class Meta:
        model=Zero_cancellation_terms
        fields="__all__"           

#....why choose us...#

class why_chooseser(serializers.ModelSerializer):
    class Meta:
        model=why_choose
        fields="__all__"

#....question...#
        


#....icic...#
        
class icic_serialization(serializers.ModelSerializer):
    class Meta:
        model=icic_offer
        fields="__all__"

class icici_serialization(serializers.ModelSerializer):
    class Meta:
        model=icic_terms
        fields="__all__"    

#...................sbi card......................

class sbiimage_serialization(serializers.ModelSerializer):
    class Meta:
        model=sbiimage
        fields="__all__"

class sbioffer_serialization(serializers.ModelSerializer):
    class Meta:
        model=sbioffer
        fields="__all__"

class sbiterms_serialization(serializers.ModelSerializer):
    class Meta:
        model=sbiterms
        fields="__all__"            

#...................hdfc card......................
        
class hdfc_logoser(serializers.ModelSerializer):
    class Meta:
        model=hdfc_logo
        fields="__all__"             
class hdfc_offerser(serializers.ModelSerializer):
    class Meta:
        model=hdfc_offer
        fields="__all__"         
      
#...................Axis  card......................


class axis_offer_serialization(serializers.ModelSerializer):
    class Meta:
        model=flight_offers7
        fields="__all__"

class axis_terms_serialization(serializers.ModelSerializer):
    class Meta:
        model=flight_offers8
        fields="__all__"



#......................HOTELS...........................#
  

from .models import *
from rest_framework import serializers



class cardsserializationclass(serializers.ModelSerializer):
    class Meta:
        model=hotel_cards
        fields= ['title', 'content', 'image', 'Book_now', 'url']
        extra_kwargs = {
            'title': {'required': False},
            'content': {'required': False},
            'image': {'required': False},
            'Book_now': {'required': False},
            'url': {'required': False}
        } 

#...Axis...#

class hotel_axis_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_axisoffer
        fields= ['image']
        extra_kwargs = {
            'image': {'required': False} 
        } 



class hotel_axispolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_axispolicy
        fields = ['content', 'content1', 'content2', 'content3', 'content4']
        extra_kwargs = {
            'content': {'required': False},
            'content1': {'required': False},
            'content2': {'required': False},
            'content3': {'required': False},
            'content4': {'required': False}
            
        } 

class hotel_axisserialization1(serializers.ModelSerializer):
    class Meta:
        model=hotel_axisoffer1
        fields= ['product', 'offer']
        extra_kwargs = {
            'product': {'required': False},
            'offer': {'required': False}
        }         

#...icici...#
        
class hotel_icici_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_icicioffer
        fields= ['image', 'title', 'couponcode']
        extra_kwargs = {
            'image': {'required': False},
            'title': {'required': False},
            'couponcode': {'required': False}
        } 



class hotel_icicipolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_icicipolicy
        fields = ['content', 'content1', 'content2', 'content3', 'content4']
        extra_kwargs = {
            'content': {'required': False},
            'content1': {'required': False},
            'content2': {'required': False},
            'content3': {'required': False},
            'content4': {'required': False}
            
        } 

class hotel_iciciserialization1(serializers.ModelSerializer):
    class Meta:
        model=hotel_icicioffer1
        fields= ['applicable', 'offer']
        extra_kwargs = {
            'applicable': {'required': False},
            'offer': {'required': False}
        }           

#...HSBC...#

class hotel_hsbc_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_hsbcoffer
        fields= ['image', 'title', 'couponcode']
        extra_kwargs = {
            'image': {'required': False},
            'title': {'required': False},
            'couponcode': {'required': False}
        }



class hotel_hsbcpolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_hsbcpolicy
        fields = ['data', 'data1', 'data2', 'data3', 'data4']
        extra_kwargs = {
            'data': {'required': False},
            'data1': {'required': False},
            'data2': {'required': False},
            'data3': {'required': False},
            'data4': {'required': False} 
        } 

class hotel_hsbcserialization1(serializers.ModelSerializer):
    class Meta:
        model=hotel_hsbcoffer1
        fields= ['applicable', 'offer']
        extra_kwargs = {
            'applicable': {'required': False},
            'offer': {'required': False}
        }                  

#...SBI....#
        
class hotel_sbi_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_sbioffer
        fields= ['image', 'title', 'couponcode']
        extra_kwargs = {
            'image': {'required': False},
            'title': {'required': False},
            'couponcode': {'required': False}
        }



class hotel_sbipolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_sbipolicy
        fields = ['cnt', 'cnt1', 'cnt2', 'cnt3', 'cnt4']
        extra_kwargs = {
            'cnt': {'required': False},
            'cnt1': {'required': False},
            'cnt2': {'required': False},
            'cnt3': {'required': False},
            'cnt4': {'required': False} 
        }  

class hotel_sbiserialization1(serializers.ModelSerializer):
    class Meta:
        model=hotel_sbioffer1
        fields= ['applicable', 'offer']
        extra_kwargs = {
            'applicable': {'required': False},
            'offer': {'required': False}
        }                 

#...KOTAK...#
        

class hotel_kotak_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_kotakoffer
        fields= ['image', 'title', 'couponcode']
        extra_kwargs = {
            'image': {'required': False},
            'title': {'required': False},
            'couponcode': {'required': False}
        }


class hotel_kotakpolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_kotakpolicy
        fields = ['cntnt', 'cntnt1', 'cntnt2', 'cntnt3']
        extra_kwargs = {
            'cntnt': {'required': False},
            'cntnt1': {'required': False},
            'cntnt2': {'required': False},
            'cntnt3': {'required': False}  
        } 

class hotel_kotakserialization1(serializers.ModelSerializer):
    class Meta:
        model=hotel_kotakoffer1
        fields= ['applicable', 'offer']
        extra_kwargs = {
            'applicable': {'required': False},
            'offer': {'required': False}
        }         

#.....BOB.....#
        

class hotel_bob_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_boboffer
        fields= ['photo', 'title', 'cpncode']
        extra_kwargs = {
            'photo': {'required': False},
            'title': {'required': False},
            'cpncode': {'required': False}
        }

class hotel_bobpolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_bobpolicy
        fields = ['term', 'term1', 'term2', 'term3']
        extra_kwargs = {
            'term': {'required': False},
            'term1': {'required': False},
            'term2': {'required': False},
            'term3': {'required': False} 
        } 

class hotel_bobserialization1(serializers.ModelSerializer):
    class Meta:
        model=hotel_boboffer1
        fields = ['category', 'couponcode', 'offer']
        extra_kwargs = {
            'category': {'required': False},
            'couponcode': {'required': False},
            'offer': {'required': False}
        }            


#...FEDERAL...#  


class hotel_federal_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_federaloffer
        fields= ['image', 'title', 'couponcode']
        extra_kwargs = {
            'image': {'required': False},
            'title': {'required': False},
            'couponcode': {'required': False}
        }



class hotel_federalpolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_federalpolicy
        fields = ['cntnt', 'cntnt1']
        extra_kwargs = {
            'cntnt': {'required': False},
            'cntnt1': {'required': False}
        }  

class hotel_federalserialization1(serializers.ModelSerializer):
    class Meta:
        model=hotel_federaloffer1
        fields= ['applicable', 'offer']
        extra_kwargs = {
            'applicable': {'required': False},
            'offer': {'required': False}
        }  



        
                      
#################################  cabs #############################
from rest_framework import serializers
from .models import *

class cab_serialization(serializers.ModelSerializer):
    class Meta:
        model = cab_cards
        fields = ['title', 'description', 'photo', 'code', 'Link']
        extra_kwargs = {
            
            'title': {'required': False},
            'description': {'required': False},
            'photo': {'required': False},
            'code': {'required': False},
            'Link': {'required': False}
        }


###############  2nd page for 1st card ##########

class festive_serialization(serializers.ModelSerializer):
    class Meta:
        model = cab_festive
        fields = ['photo', 'title', 'point1', 'point2', 'point3', 'point4', 'point5', 'point6', 'point7', 'point8', 'point9', 'point10', 'point11', 'point12']
        extra_kwargs = {

            'photo': {'required': False},
            'title': {'required': False},
            'point1': {'required': False},
            'point2': {'required': False},
            'point3': {'required': False},
            'point4': {'required': False},
            'point5': {'required': False},
            'point6': {'required': False},
            'point7': {'required': False},
            'point8': {'required': False},
            'point9': {'required': False},
            'point10': {'required': False},
            'point11': {'required': False},
            'point12': {'required': False}

        }



###############  2nd page for 2nd card ##########

class rental_serialization(serializers.ModelSerializer):
    class Meta:
        model = cab_rental
        fields = ['photo', 'title', 'point1', 'point2', 'point3', 'point4', 'point5', 'point6', 'point7', 'point8', 'point9', 'point10', 'point11', 'point12']
        extra_kwargs = {

            'photo': {'required': False},
            'title': {'required': False},
            'point1': {'required': False},
            'point2': {'required': False},
            'point3': {'required': False},
            'point4': {'required': False},
            'point5': {'required': False},
            'point6': {'required': False},
            'point7': {'required': False},
            'point8': {'required': False},
            'point9': {'required': False},
            'point10': {'required': False},
            'point11': {'required': False},
            'point12': {'required': False}
        }
###############  2nd page for 3rd card ##########

class anytime_serialization(serializers.ModelSerializer):
    class Meta:
        model = cab_anytime
        fields = ['photo', 'heading', 'content', 'title', 'point1', 'point2', 'point3', 'point4', 'point5', 'point6', 'point7', 'point8', 'point9', 'point10', 'point11', 'point12']
        extra_kwargs = {

            'photo': {'required': False},
            'heading': {'required': False},
            'content': {'required': False},
            'title': {'required': False},
            'point1': {'required': False},
            'point2': {'required': False},
            'point3': {'required': False},
            'point4': {'required': False},
            'point5': {'required': False},
            'point6': {'required': False},
            'point7': {'required': False},
            'point8': {'required': False},
            'point9': {'required': False},
            'point10': {'required': False},
            'point11': {'required': False},
            'point12': {'required': False}
        }




###############  2nd page for 4th card ##########

class ride_serialization(serializers.ModelSerializer):
    class Meta:
        model = cab_ride
        fields = ['photo', 'title', 'point1', 'point2', 'point3', 'point4', 'point5', 'point6', 'point7', 'point8', 'point9', 'point10', 'point11', 'point12']
        extra_kwargs = {

            'photo': {'required': False},
            'title': {'required': False},
            'point1': {'required': False},
            'point2': {'required': False},
            'point3': {'required': False},
            'point4': {'required': False},
            'point5': {'required': False},
            'point6': {'required': False},
            'point7': {'required': False},
            'point8': {'required': False},
            'point9': {'required': False},
            'point10': {'required': False},
            'point11': {'required': False},
            'point12': {'required': False}
        }
    


###############  2nd page for 5th card ##########


class familyfun_serialization(serializers.ModelSerializer):
    class Meta:
        model = cab_familyfun
        fields = ['photo', 'heading', 'content', 'title', 'point1', 'point2', 'point3', 'point4', 'point5', 'point6', 'point7', 'point8', 'point9', 'point10', 'point11', 'point12']
        extra_kwargs = {

            'photo': {'required': False},
            'heading': {'required': False},
            'content': {'required': False},
            'title': {'required': False},
            'point1': {'required': False},
            'point2': {'required': False},
            'point3': {'required': False},
            'point4': {'required': False},
            'point5': {'required': False},
            'point6': {'required': False},
            'point7': {'required': False},
            'point8': {'required': False},
            'point9': {'required': False},
            'point10': {'required': False},
            'point11': {'required': False},
            'point12': {'required': False}
        }




###############  2nd page for 6th card ##########

class easy_serialization(serializers.ModelSerializer):
    class Meta:
        model = cab_easy
        fields = ['photo', 'title', 'point1', 'point2', 'point3', 'point4', 'point5', 'point6', 'point7', 'point8', 'point9', 'point10', 'point11', 'point12']
        extra_kwargs = {

            'photo': {'required': False},
            'title': {'required': False},
            'point1': {'required': False},
            'point2': {'required': False},
            'point3': {'required': False},
            'point4': {'required': False},
            'point5': {'required': False},
            'point6': {'required': False},
            'point7': {'required': False},
            'point8': {'required': False},
            'point9': {'required': False},
            'point10': {'required': False},
            'point11': {'required': False},
            'point12': {'required': False}
        }





###############  2nd page for 7th card ##########

class offer15_serialization(serializers.ModelSerializer):
    class Meta:
        model = cab_offer_card
        fields = ['photo', 'title', 'point1', 'point2', 'point3', 'point4', 'point5', 'point6', 'point7', 'point8', 'point9', 'point10', 'point11', 'point12']
        extra_kwargs = {

            'photo': {'required': False},
            'title': {'required': False},
            'point1': {'required': False},
            'point2': {'required': False},
            'point3': {'required': False},
            'point4': {'required': False},
            'point5': {'required': False},
            'point6': {'required': False},
            'point7': {'required': False},
            'point8': {'required': False},
            'point9': {'required': False},
            'point10': {'required': False},
            'point11': {'required': False},
            'point12': {'required': False}
        }



###############  2nd page for 8th card ##########

class paytm_card_serialization(serializers.ModelSerializer):
    class Meta:
        model = cab_paytm_card
        fields = ['photo', 'title', 'point1', 'point2', 'point3', 'point4', 'point5', 'point6', 'point7', 'point8', 'point9', 'point10', 'point11', 'point12']
        extra_kwargs = {

            'photo': {'required': False},
            'title': {'required': False},
            'point1': {'required': False},
            'point2': {'required': False},
            'point3': {'required': False},
            'point4': {'required': False},
            'point5': {'required': False},
            'point6': {'required': False},
            'point7': {'required': False},
            'point8': {'required': False},
            'point9': {'required': False},
            'point10': {'required': False},
            'point11': {'required': False},
            'point12': {'required': False}
        }


##.....BUSES.....##

from rest_framework import serializers
from .models import *


######### trending offers cards ###########


class bus_serialization(serializers.ModelSerializer):
    class Meta:
        model=bus_offercards
        fields = '__all__'



####### card1 #######

class bus_weekends1_serialization(serializers.ModelSerializer):
    class Meta:
        model = bus_weekends1
        fields = ['heading', 'image', 'title', 'point']
        extra_kwargs = {
            'heading': {'required': False},
            'image': {'required': False},
            'title': {'required': False},
            'point': {'required': False}
        }



class bus_weekends_terms1_serialization(serializers.ModelSerializer):
    class Meta:
        model = bus_weekends_terms1
        fields = [ 'title', 'point']
        extra_kwargs = {
            'title': {'required': False},
            'point': {'required': False}
        }


#######card2######

class bus_go_image2_serialization(serializers.ModelSerializer):
    class Meta:
        model = bus_go_image2
        fields = ['image']

class bus_go_table2_serialization(serializers.ModelSerializer):
    class Meta:
        model = bus_go_table2
        fields = ['heading','title']
        extra_kwargs = {
            'heading': {'required': False},
            'title': {'required': False}
        }


class bus_go_container2_serialization(serializers.ModelSerializer):
    class Meta:
        model = bus_go_container2
        fields = ['heading','title']
        extra_kwargs = {
            'heading': {'required': False},
            'title': {'required': False}
        }


class bus_go_benefits2_serialization(serializers.ModelSerializer):
    class Meta:
        model = bus_go_benefits2
        fields = ['title']


class bus_go_cancel_serialization(serializers.ModelSerializer):
    class Meta:
        model=bus_go_cancel
        fields = '__all__'



class bus_go_terms2_serialization(serializers.ModelSerializer):
    class Meta:
        model=bus_go_terms2
        fields = '__all__'


########### card3   #####
class bus_festival3_serialization(serializers.ModelSerializer):
    class Meta:
        model = bus_festival3
        fields = ['heading', 'image', 'title', 'point']
        extra_kwargs = {
            'heading': {'required': False},
            'image': {'required': False},
            'title': {'required': False},
            'point': {'required': False}
        }

##########  card4 ########
class bus_special_code4_serialization(serializers.ModelSerializer):
    class Meta:
        model = bus_special_code4
        fields = ['heading', 'image', 'title']
        extra_kwargs = {
            'heading': {'required': False},
            'image': {'required': False},
            'title': {'required': False}
        }


class bus_special_avail4_serialization(serializers.ModelSerializer):
    class Meta:
        model = bus_special_avail4
        fields = ['heading', 'title']
        extra_kwargs = {
            'heading': {'required': False},
            'title': {'required': False}
        }

class bus_special_terms4_serialization(serializers.ModelSerializer):
    class Meta:
        model = bus_special_terms4
        fields = ['heading', 'point']
        extra_kwargs = {
            'heading': {'required': False},
            'point': {'required': False}
        }


######## card5 ######
class bus_firstbus_code5_serialization(serializers.ModelSerializer):
    class Meta:
        model = bus_firstbus_code5
        fields = ['heading',  'title', 'code', 'Image']
        extra_kwargs = {
            'heading': {'required': False},
            'title': {'required': False},
            'code': {'required': False},
            'Image': {'required': False}
        }

class bus_firstbus_get5_serialization(serializers.ModelSerializer):
    class Meta:
        model = bus_firstbus_get5
        fields = ['heading','title']
        extra_kwargs = {
            'heading': {'required': False},
            'title': {'required': False}
        }


class bus_firstbus_terms5_serialization(serializers.ModelSerializer):
    class Meta:
        model = bus_firstbus_terms5
        fields = ['title', 'point']
        extra_kwargs = {
            'title': {'required': False},
            'point': {'required': False}
        }




############# card6  ##########

class bus_busday_image6_serialization(serializers.ModelSerializer):
    class Meta:
        model = bus_busday_image6
        fields = ['image']
        extra_kwargs = {
            'image': {'required': False}
          
        }

        
class bus_busday_terms6_serialization(serializers.ModelSerializer):
    class Meta:
        model = bus_busday_terms6
        fields = [ 'heading',  'title', 'point']
        extra_kwargs = {
            'heading': {'required': False},
            'title': {'required': False},
            'point': {'required': False}
        }
            


########### card7 #############

class bus_easeday7_serialization(serializers.ModelSerializer):
       class Meta:
        model = bus_easeday7
        fields = ['photo', 'title1', 'point']
        extra_kwargs = {
            'photo': {'required': False},
            'title1': {'required': False},
            'point': {'required': False}
            
        }

    ########## card 8 #########
    

class bus_weekday8_serialization(serializers.ModelSerializer):
    class Meta:
        model = bus_weekday8
        fields = [ 'image',   'heading', 'heading1', 'heading2', 'offer', 'promocode', 'title', 'point']
        extra_kwargs = {
            
            'image': {'required': False},
            'heading': {'required': False},
            'heading1': {'required': False},
            'heading2': {'required': False},
            'offer': {'required': False},
            'promocode': {'required': False},
            'title': {'required': False},
            'point': {'required': False}
            
        }


##########  card9  ###########


class bus_offer9_serialization(serializers.ModelSerializer):
    class Meta:
        model = bus_offer9
        fields = ['title',  'description', 'image']
        extra_kwargs = {
            'title': {'required': False},
            'description': {'required': False},
            'image': {'required': False}
        }


############# card10 ##########
        
class bus_fest10_serialization(serializers.ModelSerializer):
    class Meta:
        model = bus_fest10
        fields = ['title',  'content', 'photo']
        extra_kwargs = {
            'title': {'required': False},
            'content': {'required': False},
            'photo': {'required': False}
        }


###########  card11  ###########
        
class bus_icici11_serialization(serializers.ModelSerializer):
    class Meta:
        model = bus_icici11
        fields = ['title',  'description', 'image']
        extra_kwargs = {
            'title': {'required': False},
            'description': {'required': False},
            'image': {'required': False}
        }


########### card12  ##########
        
class bus_holiday12_serialization(serializers.ModelSerializer):
    class Meta:
        model = bus_holiday12
        fields = ['title',  'description', 'image']
        extra_kwargs = {
            'title': {'required': False},
            'description': {'required': False},
            'image': {'required': False}
        }


########### card13  ##########
        
class bus_ride13_serialization(serializers.ModelSerializer):
    class Meta:
        model = bus_ride13
        fields = ['title',  'description', 'image']
        extra_kwargs = {
            'title': {'required': False},
            'description': {'required': False},
            'image': {'required': False}
        }



################ Bus Search Form ##############

class bus_searchform_serialization(serializers.ModelSerializer):
    class Meta:
        model = bus_searchform
        fields = ['From', 'To', 'Departure']
        extra_kwargs = {
            'From': {'required': False},
            'To': {'required': False},
            'Departure': {'required': False}
        }

