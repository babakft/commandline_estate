from base.baseclass import BaseClass
from estate.estate import Apartment, House, Store
from deal import Rent,Sell

class ApartmentSell(BaseClass, Apartment, Sell):

    def show_detail(self):
        self.show_description()


class ApartmentRent(BaseClass, Apartment, Rent):
    def show_detail(self):
        self.show_description()


class HouseSell(BaseClass, House, Sell):
    def show_detail(self):
        self.show_description()


class HouseRent(BaseClass, House, Rent):
    def show_detail(self):
        self.show_description()


class StoreSell(BaseClass, Store, Sell):
    def show_detail(self):
        self.show_description()


class StoreRent(BaseClass, Store, Rent):
    def show_detail(self):
        self.show_description()
