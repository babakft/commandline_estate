from base.baseclass import BaseClass
from estate.estate import Apartment, House, Store
from deal.deal_type import Rent, Sell
from estate.sellerInformation import SellerInformation

"""
tha main file all of this class use there parent method 
and combine them 
"""


class ApartmentSell(BaseClass, Apartment, Sell):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_detail(self):
        print("#" * 80)
        self.show_description()
        self.show_deal()
        print("#" * 80 + "\n")

    def insert_argument(self):
        argument_set = self.show_argument().union(self.show_sell_argument())
        insert = dict()
        for arg in argument_set:
            if str(arg) == "self" or str(arg) == "*args" or str(arg) == "**kwargs":
                continue
            else:
                insert_input = input(f"{arg}:\n")
                insert[str(arg)] = insert_input

        ApartmentSell(has_elevator=insert["has_elevator"], has_parking=insert["has_parking"], floor=insert["floor"],
                      seller_information=SellerInformation.objects_list[1],
                      area=insert["area"], room_count=insert["room_count"], build_year=insert["build_year"],
                      region=insert["region"],
                      address=insert["address"], price_per_meter=insert["price_per_meter"], discount=insert["discount"],
                      convert_able=insert["convert_able"])


class ApartmentRent(BaseClass, Apartment, Rent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_detail(self):
        print("#" * 80)
        self.show_description()
        self.show_deal()
        print("#" * 80 + "\n")

    def insert_argument(self):
        argument_set = self.show_argument().union(self.show_rent_argument())
        insert = dict()
        for arg in argument_set:
            if str(arg) == "self" or str(arg) == "*args" or str(arg) == "**kwargs":
                continue
            else:
                insert_input = input(f"{arg}:\n")
                insert[str(arg)] = insert_input

        ApartmentRent(
            has_elevator=insert["has_elevator"], has_parking=insert["has_parking"], floor=insert["floor"],
            seller_information=SellerInformation.objects_list[1],
            build_year=insert["build_year"], region=insert["region"], area=insert["area"],
            room_count=insert["room_count"],
            initial_price=insert["initial_price"], rent_price=insert["rent_price"],
            address=insert["address"], discount=insert["discount"]
        )


class HouseSell(BaseClass, House, Sell):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_detail(self):
        print("#" * 80)
        self.show_description()
        self.show_deal()
        print("#" * 80 + "\n")

    def insert_argument(self):
        argument_set = self.show_argument().union(self.show_sell_argument())
        insert = dict()
        for arg in argument_set:
            if str(arg) == "self" or str(arg) == "*args" or str(arg) == "**kwargs":
                continue
            else:
                insert_input = input(f"{arg}:\n")
                insert[str(arg)] = insert_input

        HouseSell(
            has_yard=insert["has_yard"], floor=insert["floor"], seller_information=SellerInformation.objects_list[0],
            area=insert["area"],
            room_count=insert["room_count"], build_year=insert["build_year"], region=insert["region"],
            address=insert["address"],
            price_per_meter=insert["price_per_meter"], discount=insert["discount"], convert_able=insert["convert_able"]
        )


class HouseRent(BaseClass, House, Rent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_detail(self):
        print("#" * 80)
        self.show_description()
        self.show_deal()
        print("#" * 80 + "\n")

    def insert_argument(self):
        argument_set = self.show_argument().union(self.show_rent_argument())
        insert = dict()
        for arg in argument_set:
            if str(arg) == "self" or str(arg) == "*args" or str(arg) == "**kwargs":
                continue
            else:
                insert_input = input(f"{arg}:\n")
                insert[str(arg)] = insert_input
        HouseRent(
            has_yard=insert["has_yard"], floor=insert["floor"], seller_information=SellerInformation.objects_list[2],
            area=insert["area"],
            room_count=insert["room_count"], build_year=insert["build_year"], region=insert["region"],
            address=insert["address"],
            initial_price=insert["initial_price"], rent_price=insert["rent_price"], discount=insert["discount"])


class StoreSell(BaseClass, Store, Sell):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_detail(self):
        print("#" * 80)
        self.show_description()
        self.show_deal()
        print("#" * 80 + "\n")

    def insert_argument(self):
        argument_set = self.show_argument().union(self.show_sell_argument())
        insert = dict()
        for arg in argument_set:
            if str(arg) == "self" or str(arg) == "*args" or str(arg) == "**kwargs":
                continue
            else:
                insert_input = input(f"{arg}:\n")
                insert[str(arg)] = insert_input

        StoreSell(seller_information=SellerInformation.objects_list[1],
                  area=insert["area"], room_count=insert["room_count"], build_year=insert["build_year"],
                  region=insert["region"], address=insert["address"],
                  price_per_meter=insert["price_per_meter"], discount=insert["discount"],
                  convert_able=insert["convert_able"]
                  )


class StoreRent(BaseClass, Store, Rent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_detail(self):
        print("#" * 80)
        self.show_description()
        self.show_deal()
        print("#" * 80 + "\n")

    def insert_argument(self):
        argument_set = self.show_argument().union(self.show_rent_argument())
        insert = dict()
        for arg in argument_set:
            if str(arg) == "self" or str(arg) == "*args" or str(arg) == "**kwargs":
                continue
            else:
                insert_input = input(f"{arg}:\n")
                insert[str(arg)] = insert_input

        StoreRent(seller_information=SellerInformation.objects_list[1],
                  area=insert["area"], room_count=insert["room_count"], build_year=insert["build_year"],
                  region=insert["region"],
                  address=insert["address"],
                  initial_price=insert["initial_price"], rent_price=insert["rent_price"], discount=insert["discount"])
