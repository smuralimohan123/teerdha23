from django.db import models

# Create your models here.

#....dashboard_curdoprations....#
# class dashboard_sidebar(models.Model):
#     title = models.CharField(max_length=100)
#     url = models.CharField(max_length=255)
#     icon = models.CharField(max_length=100)
#     category=models.CharField(max_length=100,default="")
# class Mets:
#     db_table="dashboard_sidebar"


# class profile(models.Model):
#     image=models.ImageField(upload_to='media/')


from django.contrib.auth.models import User


class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    bio = models.TextField(blank=True)
    email = models.EmailField(max_length=255, blank=True)
    mobile_number = models.CharField(max_length=20, blank=True)
class Meta:
    db_table="Profiles"




class crudoperations(models.Model):
    card=models.CharField(max_length=100)
    url=models.URLField()
class Meta:
    db_table="crudoperations"

class Naviagtion_bar(models.Model):
    name=models.CharField(max_length=100)
    icon=models.ImageField(upload_to='media/',default='')
    url=models.URLField()
class Meta:
    db_table="Navigation_bar"

class Home_carousel(models.Model):
    image=models.ImageField(upload_to='media/')
    class Meta:
        db_table="Home_carousel"


class Contact(models.Model):
      Name=models.CharField(max_length=100)
      Email=models.EmailField(max_length = 500)
      Phonenumber=models.BigIntegerField()
      Message=models.TextField()
      Subject=models.CharField(max_length=1000)
class Meta:
    db_table="Contact"  



###############################      flights_data       ##########################################

# Create your models here.

class flights_offerscrudoperations(models.Model):
    offer=models.CharField(max_length=100)
    url=models.URLField() 
class Meta:
    db_table="flights_offerscrudoperations"    


class flights_offercards(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=100,default=None)
    image=models.ImageField(upload_to="images/")
    logo=models.ImageField(upload_to="images/",default=None)
    url=models.URLField(default="")
class Meta:
    db_table="flights_offercards"

class flights_kotak_offer(models.Model):
    image=models.ImageField(upload_to="media/")
    # logo=models.ImageField(upload_to="media/")
    text=models.CharField(max_length=100)
    text1=models.CharField(max_length=100)

    class Meta:
        db_table="flights_kotak_offer"

class flights_kotak_terms(models.Model):
    terms=models.TextField()
    condition=models.TextField(default="")

    class Meta:
        db_table="flights_kotak_terms"

class flights_policy(models.Model):
    content=models.TextField()
    class Meta:
        db_table="flights_policy"

class flights_policy1(models.Model):
    content1=models.TextField()
    class Meta:
        db_table="flights_policy1"
    
class flights_kotak_offer1(models.Model):
    image1=models.ImageField(upload_to="media/")
    category=models.CharField(max_length=100)
    couponcode=models.CharField(max_length=100)
    offer=models.CharField(max_length=100)

    class Meta:
        db_table="flights_kotak_offer1"

### first booking ###

class flight_offer_first(models.Model):
    image=models.ImageField(upload_to="images/")
    content=models.CharField(max_length=255)
class Meta:
    db_table="flight_offer_first"
        
class flight_offer_first1(models.Model):
    title=models.CharField(max_length=255,default=None)
    content=models.TextField()
class Meta:
    db_table="flight_offer_first1"


### .....Yes Bank offer_cards Detailes   models

class card1_offers(models.Model):
    logo1=models.ImageField(upload_to="images/",null=True,blank=True)
    image=models.ImageField(upload_to="images/",null=True,blank=True)
    logo2=models.ImageField(upload_to="images/",null=True,blank=True)
    title=models.CharField(max_length=400)
    content=models.CharField(max_length=500)
class Meta:
    db_table="card1_offers"

class card1_offerdetailes(models.Model):
    type=models.CharField(max_length=200,null=True,blank=True)
    PromoCode=models.CharField(max_length=400)
    offer=models.CharField(max_length=300)
    Applicable_on=models.CharField(max_length=400)
class Meta:
    db_table="card1_offerdetailes"

class card1_terms_conditions(models.Model):
    title=models.CharField(max_length=400,null=True,blank=True)
    content=models.TextField()
class Meta:
    db_table="card1_terms_conditions"    

## FAQ ##    
    

##...refundcrads...##

class Zero_cancellation_offer(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images/")
    content1=models.CharField(max_length=200)
    content2=models.CharField(max_length=200)
    logo1=models.ImageField(upload_to="images/",blank=True)
    logo2=models.ImageField(upload_to="images/",blank=True)
class Meta:
    db_table="Zero_cancellation_offer"


class Zero_cancellation_terms(models.Model):
    title=models.CharField(max_length=200,blank=True)
    content=models.TextField()
class Meta:
    db_table="Zero_cancellation_terms"     

#....why choose us.....#
    
class why_choose(models.Model):
    image=models.ImageField(upload_to="images/") 
    content=models.CharField(max_length=200)
class Meta:
    db_table="why_choose"


#...questions...#
    
class choosing_content(models.Model):
    question=models.CharField(max_length=100)
    answer=models.TextField()

    class Meta:
        db_table="choosing_content"    

#....icici...#
        
class icic_offer(models.Model):
    title=models.CharField(max_length=250)
    image=models.ImageField(upload_to="images/")
    content1=models.CharField(max_length=250)
    content2=models.CharField(max_length=250)
    logo1=models.ImageField(upload_to="images/",blank=True)
    logo2=models.ImageField(upload_to="images/",blank=True)
class Meta:
    db_table="icic_offer"


class icic_terms(models.Model):
    title=models.CharField(max_length=200,blank=True)
    content=models.TextField()
class Meta:
    db_table="icic_terms"        
    
##....SBI Card Offer.....#

class sbiimage(models.Model):
    image=models.ImageField(upload_to="images/")
    class Meta:
        db_table="sbiimage"
        
class sbioffer(models.Model):
    type=models.CharField(max_length=100)
    offer=models.CharField(max_length=200)
    min_amt=models.CharField(max_length=100)
    Promo_Code=models.CharField(max_length=100)
class Meta:
    db_table="sbioffer"

class sbiterms(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
class Meta:
    db_table="sbiterms"    


class hdfc_logo(models.Model):
    title=models.ImageField(upload_to="images/")
class Meta:
    db_table="hdfc_logo"
    
class hdfc_offer(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
class Meta:
    db_table="hdfc_offer"    



class flight_offers7(models.Model):
   photo=models.ImageField(upload_to="images/")
   heading=models.CharField(max_length=100,default='')
   content=models.CharField(max_length=100,default='')
   title=models.CharField(max_length=100,default='')
   point = models.TextField(help_text="Enter product info on a new line.",default='')
   
class Meta:
    db_table="flight_offers7"

class flight_offers8(models.Model):
   heading=models.CharField(max_length=100,default='')
   photo1=models.ImageField(upload_to="media/")
   title=models.CharField(max_length=100,default='')
   description=models.CharField(max_length=100,default='') 
class Meta:
    db_table="flight_offers8"
 

 ##.....................Hotels..................##
    
from django.db import models

# Create your models here.
class hotel_cards(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=1000)
    image=models.ImageField(upload_to="media/")
    Book_now=models.CharField(max_length=1000,default='')
    url=models.URLField(default="")
class Meta:
        db_table="hotel_cards"

class hotel_quary(models.Model):
    ques=models.TextField()
    ans=models.TextField()
    class Meta:
        db_table="hotel_quary"    

class hotel_faqitem(models.Model):
    question = models.TextField()
    answer = models.TextField()    
    class Meta:
        db_table="hotel_faqitem"

#...axis_offer...#
    

class hotel_axisoffer(models.Model):
    image=models.ImageField(upload_to="media/")
    
    class Meta:
        db_table="hotel_axisoffer"


class hotel_axispolicy(models.Model):
    content=models.TextField()
    content1=models.TextField()
    content2=models.TextField()
    content3=models.TextField()
    content4=models.TextField(default="")

    class Meta:
        db_table="hotel_axispolicy"

    
class hotel_axisoffer1(models.Model):
    product=models.CharField(max_length=100)
    offer=models.CharField(max_length=100)

    class Meta:
        db_table="hotel_axisoffer1"


#...icici...#
        
class hotel_icicioffer(models.Model):
    image=models.ImageField(upload_to="media/")
    title=models.CharField(max_length=100)
    couponcode=models.CharField(max_length=100)
    class Meta:
        db_table="hotel_icicioffer"


class hotel_icicipolicy(models.Model):
    content=models.TextField()
    content1=models.TextField()
    content2=models.TextField()
    content3=models.TextField()
    content4=models.TextField(default="")

    class Meta:
        db_table="hotel_icicipolicy"

    
class hotel_icicioffer1(models.Model):
    applicable=models.CharField(max_length=100)
    offer=models.CharField(max_length=100)

    class Meta:
        db_table="hotel_icicioffer1"
        
#...HSBC...#

class hotel_hsbcoffer(models.Model):
    image=models.ImageField(upload_to="media/")
    title=models.CharField(max_length=100)
    couponcode=models.CharField(max_length=100)
    class Meta:
        db_table="hotel_hsbcoffer"


class hotel_hsbcpolicy(models.Model):
    data=models.TextField()
    data1=models.TextField()
    data2=models.TextField()
    data3=models.TextField()
    data4=models.TextField()

    class Meta:
        db_table="hotel_hsbcpolicy"

    
class hotel_hsbcoffer1(models.Model):
    applicable=models.CharField(max_length=100)
    offer=models.CharField(max_length=100)

    class Meta:
        db_table="hotel_hsbcoffer1"     

#...SBI...#

class hotel_sbioffer(models.Model):
    image=models.ImageField(upload_to="media/")
    title=models.CharField(max_length=100)
    couponcode=models.CharField(max_length=100)
    class Meta:
        db_table="hotel_sbioffer"


class hotel_sbipolicy(models.Model):
    cnt=models.TextField()
    cnt1=models.TextField()
    cnt2=models.TextField()
    cnt3=models.TextField()
    cnt4=models.TextField()

    class Meta:
        db_table="hotel_sbipolicy"

    
class hotel_sbioffer1(models.Model):
    applicable=models.CharField(max_length=100)
    offer=models.CharField(max_length=100)

    class Meta:
        db_table="hotel_sbioffer1"                                           

#...KOTAK...#


class hotel_kotakoffer(models.Model):
    image=models.ImageField(upload_to="media/")
    title=models.CharField(max_length=100)
    couponcode=models.CharField(max_length=100)
    class Meta:
        db_table="hotel_kotakoffer"


class hotel_kotakpolicy(models.Model):
    cntnt=models.TextField()
    cntnt1=models.TextField()
    cntnt2=models.TextField()
    cntnt3=models.TextField()

    class Meta:
        db_table="hotel_kotakpolicy"

    
class hotel_kotakoffer1(models.Model):
    applicable=models.CharField(max_length=100)
    offer=models.CharField(max_length=100)

    class Meta:
        db_table="hotel_kotakoffer1"                                                           

#.....BOB......#
        
class hotel_boboffer(models.Model):
    photo=models.ImageField(upload_to="media/")
    title=models.CharField(max_length=100)
    cpncode=models.CharField(max_length=100)
    class Meta:
        db_table="hotel_boboffer"


class hotel_bobpolicy(models.Model):
    term=models.TextField()
    term1=models.TextField()
    term2=models.TextField()
    term3=models.TextField()

    class Meta:
        db_table="hotel_bobpolicy"

    
class hotel_boboffer1(models.Model):
    category=models.CharField(max_length=100)
    couponcode=models.CharField(max_length=100)
    offer=models.CharField(max_length=100)

    class Meta:
        db_table="hotel_boboffer1"                                                           
  


#...FEDERAL...#


class hotel_federaloffer(models.Model):
    image=models.ImageField(upload_to="media/")
    title=models.CharField(max_length=100)
    couponcode=models.CharField(max_length=100)
    class Meta:
        db_table="hotel_federaloffer"


class hotel_federalpolicy(models.Model):
    cntnt=models.TextField()
    cntnt1=models.TextField()
    

    class Meta:
        db_table="hotel_federalpolicy"

    
class hotel_federaloffer1(models.Model):
    applicable=models.CharField(max_length=100)
    offer=models.CharField(max_length=100)

    class Meta:
        db_table="hotel_federaloffer1"   


##################### cab search form #####################

class CabBooking(models.Model):
    from_city = models.CharField(max_length=100)
    to_city = models.CharField(max_length=100)
    departure_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    pickup_time = models.TimeField(null=True, blank=True)
    drop_time = models.TimeField(null=True, blank=True)
    class Meta:
        db_table = "CabBooking"

#################### cab offer cards ######################

class cab_cards(models.Model):
    title=models.CharField(max_length=100,default='')
    description=models.CharField(max_length=100,default='')
    photo=models.ImageField(upload_to="images/")
    code=models.CharField(max_length=100,default='')
    Link = models.CharField(max_length=100,default='')
    class Meta:
        db_table="cab_cards"


########################  2nd page for 1st card #######################


class cab_festive(models.Model):
    photo=models.ImageField(upload_to="images/", default='default_image.jpg')
    title=models.CharField(max_length=100,default='')
    point1 = models.TextField(help_text="Enter product info on a new line.",default='')
    point2 = models.TextField(help_text="Enter product info on a new line.",default='')
    point3 = models.TextField(help_text="Enter product info on a new line.",default='')
    point4 = models.TextField(help_text="Enter product info on a new line.",default='')
    point5 = models.TextField(help_text="Enter product info on a new line.",default='')
    point6 = models.TextField(help_text="Enter product info on a new line.",default='')
    point7 = models.TextField(help_text="Enter product info on a new line.",default='')
    point8 = models.TextField(help_text="Enter product info on a new line.",default='')
    point9 = models.TextField(help_text="Enter product info on a new line.",default='')
    point10 = models.TextField(help_text="Enter product info on a new line.",default='')
    point11 = models.TextField(help_text="Enter product info on a new line.",default='')
    point12 = models.TextField(help_text="Enter product info on a new line.",default='')
   
class Meta:
    db_table="cab_festive"




########################  2nd page for 2nd card #######################




class cab_rental(models.Model):
    photo=models.ImageField(upload_to="images/", default='')
    title=models.CharField(max_length=100,default='')
    point1 = models.TextField(help_text="Enter product info on a new line.",default='')
    point2 = models.TextField(help_text="Enter product info on a new line.",default='')
    point3 = models.TextField(help_text="Enter product info on a new line.",default='')
    point4 = models.TextField(help_text="Enter product info on a new line.",default='')
    point5 = models.TextField(help_text="Enter product info on a new line.",default='')
    point6 = models.TextField(help_text="Enter product info on a new line.",default='')
    point7 = models.TextField(help_text="Enter product info on a new line.",default='')
    point8 = models.TextField(help_text="Enter product info on a new line.",default='')
    point9 = models.TextField(help_text="Enter product info on a new line.",default='')
    point10 = models.TextField(help_text="Enter product info on a new line.",default='')
    point11 = models.TextField(help_text="Enter product info on a new line.",default='')
    point12 = models.TextField(help_text="Enter product info on a new line.",default='')

    class Meta:
        db_table = "cab_rental"
########################  2nd page for 3rd card #######################


class cab_anytime(models.Model):
    photo=models.ImageField(upload_to="images/", default='')
    heading=models.CharField(max_length=100,default='')
    content=models.CharField(max_length=100,default='')
    title=models.CharField(max_length=100,default='')
    point1 = models.TextField(help_text="Enter product info on a new line.",default='')
    point2 = models.TextField(help_text="Enter product info on a new line.",default='')
    point3 = models.TextField(help_text="Enter product info on a new line.",default='')
    point4 = models.TextField(help_text="Enter product info on a new line.",default='')
    point5 = models.TextField(help_text="Enter product info on a new line.",default='')
    point6 = models.TextField(help_text="Enter product info on a new line.",default='')
    point7 = models.TextField(help_text="Enter product info on a new line.",default='')
    point8 = models.TextField(help_text="Enter product info on a new line.",default='')
    point9 = models.TextField(help_text="Enter product info on a new line.",default='')
    point10 = models.TextField(help_text="Enter product info on a new line.",default='')
    point11 = models.TextField(help_text="Enter product info on a new line.",default='')
    point12 = models.TextField(help_text="Enter product info on a new line.",default='')
   
class Meta:
    db_table="cab_anytime"

########################  2nd page for 4thd card #######################

class cab_ride(models.Model): 
    photo=models.ImageField(upload_to="images/", default='')
    title=models.CharField(max_length=100,default='')
    point1 = models.TextField(help_text="Enter product info on a new line.",default='')
    point2 = models.TextField(help_text="Enter product info on a new line.",default='')
    point3 = models.TextField(help_text="Enter product info on a new line.",default='')
    point4 = models.TextField(help_text="Enter product info on a new line.",default='')
    point5 = models.TextField(help_text="Enter product info on a new line.",default='')
    point6 = models.TextField(help_text="Enter product info on a new line.",default='')
    point7 = models.TextField(help_text="Enter product info on a new line.",default='')
    point8 = models.TextField(help_text="Enter product info on a new line.",default='')
    point9 = models.TextField(help_text="Enter product info on a new line.",default='')
    point10 = models.TextField(help_text="Enter product info on a new line.",default='')
    point11 = models.TextField(help_text="Enter product info on a new line.",default='')
    point12 = models.TextField(help_text="Enter product info on a new line.",default='')
    
class Meta:
    db_table="cab_ride"





########################  2nd page for 5th card #######################


class cab_familyfun(models.Model):
    photo=models.ImageField(upload_to="images/", default='')
    heading=models.CharField(max_length=100,default='')
    content=models.CharField(max_length=100,default='')
    title=models.CharField(max_length=100,default='')
    point1 = models.TextField(help_text="Enter product info on a new line.",default='')
    point2 = models.TextField(help_text="Enter product info on a new line.",default='')
    point3 = models.TextField(help_text="Enter product info on a new line.",default='')
    point4 = models.TextField(help_text="Enter product info on a new line.",default='')
    point5 = models.TextField(help_text="Enter product info on a new line.",default='')
    point6 = models.TextField(help_text="Enter product info on a new line.",default='')
    point7 = models.TextField(help_text="Enter product info on a new line.",default='')
    point8 = models.TextField(help_text="Enter product info on a new line.",default='')
    point9 = models.TextField(help_text="Enter product info on a new line.",default='')
    point10 = models.TextField(help_text="Enter product info on a new line.",default='')
    point11 = models.TextField(help_text="Enter product info on a new line.",default='')
    point12 = models.TextField(help_text="Enter product info on a new line.",default='')
   
class Meta:
    db_table="cab_familyfun"


###################  2nd page for 6th card #################


class cab_easy(models.Model):
   photo=models.ImageField(upload_to="images/")
   title=models.CharField(max_length=100,default='')
   point1 = models.TextField(help_text="Enter product info on a new line.",default='')
   point2 = models.TextField(help_text="Enter product info on a new line.",default='')
   point3 = models.TextField(help_text="Enter product info on a new line.",default='')
   point4 = models.TextField(help_text="Enter product info on a new line.",default='')
   point5 = models.TextField(help_text="Enter product info on a new line.",default='')
   point6 = models.TextField(help_text="Enter product info on a new line.",default='')
   point7 = models.TextField(help_text="Enter product info on a new line.",default='')
   point8 = models.TextField(help_text="Enter product info on a new line.",default='')
   point9 = models.TextField(help_text="Enter product info on a new line.",default='')
   point10 = models.TextField(help_text="Enter product info on a new line.",default='')
   point11 = models.TextField(help_text="Enter product info on a new line.",default='')
   point12 = models.TextField(help_text="Enter product info on a new line.",default='')
   
class Meta:
    db_table="cab_easy"


###################  2nd page for 7th card #################



class cab_offer_card(models.Model):
    photo=models.ImageField(upload_to="images/", default='default_image.jpg')
    title=models.CharField(max_length=100,default='')
    point1 = models.TextField(help_text="Enter product info on a new line.",default='')
    point2 = models.TextField(help_text="Enter product info on a new line.",default='')
    point3 = models.TextField(help_text="Enter product info on a new line.",default='')
    point4 = models.TextField(help_text="Enter product info on a new line.",default='')
    point5 = models.TextField(help_text="Enter product info on a new line.",default='')
    point6 = models.TextField(help_text="Enter product info on a new line.",default='')
    point7 = models.TextField(help_text="Enter product info on a new line.",default='')
    point8 = models.TextField(help_text="Enter product info on a new line.",default='')
    point9 = models.TextField(help_text="Enter product info on a new line.",default='')
    point10 = models.TextField(help_text="Enter product info on a new line.",default='')
    point11 = models.TextField(help_text="Enter product info on a new line.",default='')
    point12 = models.TextField(help_text="Enter product info on a new line.",default='')
   
class Meta:
    db_table="cab_offer_card"



###################  2nd page for 7th card #################



class cab_paytm_card(models.Model):
    photo=models.ImageField(upload_to="images/", default='default_image.jpg')
    title=models.CharField(max_length=100,default='')
    point1 = models.TextField(help_text="Enter product info on a new line.",default='')
    point2 = models.TextField(help_text="Enter product info on a new line.",default='')
    point3 = models.TextField(help_text="Enter product info on a new line.",default='')
    point4 = models.TextField(help_text="Enter product info on a new line.",default='')
    point5 = models.TextField(help_text="Enter product info on a new line.",default='')
    point6 = models.TextField(help_text="Enter product info on a new line.",default='')
    point7 = models.TextField(help_text="Enter product info on a new line.",default='')
    point8 = models.TextField(help_text="Enter product info on a new line.",default='')
    point9 = models.TextField(help_text="Enter product info on a new line.",default='')
    point10 = models.TextField(help_text="Enter product info on a new line.",default='')
    point11 = models.TextField(help_text="Enter product info on a new line.",default='')
    point12 = models.TextField(help_text="Enter product info on a new line.",default='')
   
class Meta:
    db_table="cab_paytm_card"



####################### Why Choose content on cabs #################


class cabwhycontents(models.Model):
    ctitle=models.TextField()
    heading1=models.TextField()
   
class Meta:
    db_table='cabwhycontents'


####################### faqs on cabs #################



class cab_faq(models.Model):

    content =models.CharField(max_length=100, default='')
    Title = models.CharField(max_length=100, default='')
    description = models.TextField(help_text="Enter product info on a new line.", default='', null=True, blank=True)
    def get_description_list(self):
        return self.description.split('\n')
    class Meta:
        db_table = "cab_faq"

###....BUSES....###



###........BUSES.........###

from django.db import models

# Create your models here.


########## bus_trending offers ########

class bus_offercards(models.Model):
    image=models.ImageField(upload_to="images/")
    heading=models.CharField(max_length=100,default='')
    title=models.CharField(max_length=100)
    discount = models.TextField(max_length=255,default='')
    valid = models.TextField(max_length=255,default='')
    code = models.TextField(max_length=255,default='')
    Link = models.CharField(max_length=100,default='')
class Meta:
    db_table="bus_offercards"



############# card1 ########
    
class bus_weekends1(models.Model):
    heading=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images/", default='')
    title=models.CharField(max_length=100)
    point = models.CharField(max_length=255,default='')
    def str(self):
        return f"{self.title} - {self.point}"
class Meta:
    db_table="bus_weekends1"



class bus_weekends_terms1(models.Model):
    title=models.CharField(max_length=100)
    point = models.TextField(default='')
    def str(self):
        return f"{self.title} - {self.point}"
class Meta:
    db_table="bus_weekends_terms1"


###############  card2  ############
    

class bus_go_image2(models.Model):
    image=models.ImageField(upload_to="images/")      
class Meta:
    db_table="bus_go_image2"



class bus_go_table2(models.Model):
    heading=models.CharField(max_length=100,default='')
    title=models.CharField(max_length=100)   
class Meta:
    db_table="bus_go_table2"



class bus_go_container2(models.Model):
    heading=models.CharField(max_length=100,default='')
    title=models.CharField(max_length=100) 
class Meta:
    db_table="bus_go_container2"




class bus_go_benefits2(models.Model):  
    title=models.CharField(max_length=100)  
class Meta:
    db_table="bus_go_benefits2"


class bus_go_cancel(models.Model):
   title=models.CharField(max_length=100,default='')
   point = models.TextField(help_text="Enter product info on a new line.",default='')
class Meta:
    db_table="bus_go_cancel"


class bus_go_terms2(models.Model):
   title=models.CharField(max_length=100,default='')
   point1 = models.TextField(help_text="Enter product info on a new line.",default='')
class Meta:
    db_table="bus_go_terms2"


##########  card3  ########
        
class bus_festival3(models.Model):
    heading=models.CharField(max_length=100,default='')
    image=models.ImageField(upload_to="images/")
    title=models.CharField(max_length=100)
    point = models.TextField(max_length=255,default='')
    def str(self):
        return f"{self.title} - {self.point}"
class Meta:
    db_table="bus_festival3"


##########  card4  #########
    

class bus_special_code4(models.Model):
    heading=models.CharField(max_length=100,default='')
    image=models.ImageField(upload_to="images/")
    title=models.CharField(max_length=100)   
class Meta:
    db_table="bus_special_code4"



class bus_special_avail4(models.Model):
    heading=models.CharField(max_length=100,default='')
    title=models.CharField(max_length=100)   
class Meta:
    db_table="bus_special_avail4"


class bus_special_terms4(models.Model):
    heading=models.CharField(max_length=255,default='')
    point=models.TextField()   
class Meta:
    db_table="bus_special_terms4"


##############  card5  #########

class bus_firstbus_code5(models.Model):
    heading=models.CharField(max_length=100,default='')
    title=models.CharField(max_length=100)
    code=models.CharField(max_length=100)
    Image=models.ImageField(upload_to="images/")
    def str(self):
        return f"{self.title} - {self.code}"
class Meta:
    db_table="bus_firstbus_code5"


class bus_firstbus_get5(models.Model):                    
    heading=models.CharField(max_length=100,default='')
    title=models.CharField(max_length=255,default='')
class Meta:
        db_table='bus_firstbus_get5'


class bus_firstbus_terms5(models.Model):
    title=models.CharField(max_length=100)
    point=models.CharField(max_length=255)
    def str(self):
        return f"{self.title} - {self.point}"
class Meta:
    db_table="bus_firstbus_terms5"


######### card6 ########


class bus_busday_image6(models.Model):
    image=models.ImageField(upload_to="images/")
class Meta:
    db_table="bus_busday_image6"



class bus_busday_terms6(models.Model):
    heading=models.CharField(max_length=100,default='')
    title=models.CharField(max_length=100)
    point = models.CharField(max_length=255,default='')
    def str(self):
        return f"{self.title} - {self.point}"
class Meta:
    db_table="bus_busday_terms6"


######### card7 #########

class bus_easeday7(models.Model):
   photo=models.ImageField(upload_to="images/",default='')
   title1=models.CharField(max_length=100,default='')
   point = models.TextField()
    
class Meta:
    db_table="bus_easeday7"


############ card8   ###########
    

class bus_weekday8(models.Model):
    image=models.ImageField(upload_to="images/",default='')
    heading=models.CharField(max_length=100,default='')
    heading1=models.CharField(max_length=100,default='')
    heading2=models.CharField(max_length=100,default='')
    offer=models.CharField(max_length=100,default='')
    promocode=models.CharField(max_length=100,default='')
    title=models.CharField(max_length=100,default='')
    point = models.TextField(default='')
  
class Meta:
    db_table="bus_weekday8"


##########  card9   ##########

class bus_offer9(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField(upload_to="images/",default="")
class Meta:
    db_table="bus_offer9"   


############ card 10 ########
    
class bus_fest10(models.Model):
    title=models.CharField(max_length=255,default='')
    content=models.TextField()
    photo=models.ImageField(upload_to="images/")
class meta:
    db_table="bus_fest10"

########### card11#######

class bus_icici11(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField(upload_to="images/",default="")
class Meta:
    db_table="bus_icici11"
   
#########  card 12  #########
    
class bus_holiday12(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField(upload_to="images/",default="")
class Meta:
    db_table="bus_holiday12"


######### card13 ##########
    
class bus_ride13(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField(upload_to="images/",default="")
class Meta:
    db_table="bus_ride13"


############ BUS FAQ  TEERDHA #############

class bus_faq(models.Model):
    description1 = models.TextField(help_text="Enter product info on a new line.",default='')
    def get_description1_list(self):
        return self.description1.split('\n')
    description2 = models.TextField(help_text="Enter product info on a new line.",default='')
    def get_description2_list(self):
        return self.description2.split('\n')
class Meta:
    db_table="bus_faq"



########### why choose us #######
    
class bus_whychoose(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
class Meta:
    db_table="bus_whychoose"


############### Bus search form ############


class bus_searchform(models.Model):
    From = models.CharField(max_length=100)
    To = models.CharField(max_length=100)
    Departure = models.DateTimeField()
class Meta:
    db_table="bus_searchform"


####     nav bar    ####

class navbar(models.Model):
    photo=models.ImageField(upload_to="images/",default="")
    title=models.CharField(max_length=100)
    url=models.URLField()
    icon=models.CharField(max_length=100, default='')
class Meta:
    db_table="navbar"




class flightfaqs(models.Model):
   question=models.CharField(max_length=250)
   answer=models.TextField()

class Meta:
    db_table='flightfaqs' 


      ##################   CABS DASHBOARD DATA ################


    
class cabs_offerscrud_dashboard(models.Model):
    offer=models.CharField(max_length=100)
    url=models.URLField() 
class Meta:
    db_table="cabs_offerscrud_dashboard"    


     ##################   CABS DASHBOARD DATA ################

class cabs_secondpage_dashboard(models.Model):
    offer = models.CharField(max_length=100)
    url_insert = models.URLField()
    offer_data = models.CharField(max_length=100, default="")
    url_update = models.URLField()

    class Meta:
        db_table = "cabs_secondpage_dashboard"

  ##################   BUSES DASHBOARD DATA ################

class buses_2ndpages(models.Model):
    offer=models.CharField(max_length=100)
    inserturl=models.URLField() 
    updateurl=models.URLField()
class Meta:
    db_table="buses_2ndpages" 



class hotels_offerscrudoperations(models.Model):
    offer=models.CharField(max_length=100)
    url=models.URLField() 
class Meta:
    db_table="hotels_offerscrudoperations" 


class buses_offerscrudoperations(models.Model):
    offer=models.CharField(max_length=100)
    url=models.URLField() 
class Meta:
    db_table="buses_offerscrudoperations" 


class hotels_2ndpages(models.Model):
    offer=models.CharField(max_length=100)
    inserturl=models.URLField() 
    updateurl=models.URLField()
class Meta:
    db_table="hotels_2ndpages" 


class flights_2ndpages(models.Model):
    offer=models.CharField(max_length=100)
    inserturl=models.URLField() 
    updateurl=models.URLField()
class Meta:
    db_table="flights_2ndpages" 
    
class flights_2npdpages_update(models.Model):
    offer=models.CharField(max_length=100)
    url=models.URLField() 
class Meta:
    db_table="flights_2npdpages_update" 



class sidebar_dashboard(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    icon = models.CharField(max_length=100)
    subdivision=models.CharField(max_length=100,default='')
class Meta:
    db_table="sidebar_dashboard"
    