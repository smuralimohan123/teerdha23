from .models import Naviagtion_bar
def Navigationbar(request):
    navigation_items=Naviagtion_bar.objects.all()
    return {'navigation_items':navigation_items}