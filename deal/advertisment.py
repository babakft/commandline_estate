from base.baseclass import BaseClass
from estate.estate import Apartment, House, Store
from deal.deal_type import Rent,Sell

class ApartmentSell(BaseClass, Apartment, Sell):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def show_detail(self):
        print("#" * 80)
        self.show_description()
        self.show_deal()
        print("#"* 80 +"\n")



class ApartmentRent(BaseClass, Apartment, Rent):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def show_detail(self):
        print("#" * 80)
        self.show_description()
        self.show_deal()
        print("#" * 80 +"\n")
class HouseSell(BaseClass, House, Sell):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def show_detail(self):
        print("#" * 80)
        self.show_description()
        self.show_deal()
        print("#" * 80 +"\n")


class HouseRent(BaseClass, House, Rent):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def show_detail(self):
        print("#" * 80)
        self.show_description()
        self.show_deal()
        print("#" * 80 +"\n")


class StoreSell(BaseClass, Store, Sell):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def show_detail(self):
        print("#" * 80)
        self.show_description()
        self.show_deal()
        print("#" * 80 +"\n")



class StoreRent(BaseClass, Store, Rent):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def show_detail(self):
        print("#" * 80)
        self.show_description()
        self.show_deal()
        print("#" * 80 +"\n")
