import inspect
from estate.sellerInformation import SellerInformation
from estate.sellerInformation import SellerInformation
from deal.deal_type import Rent,Sell
from deal.advertisment import ApartmentSell,ApartmentRent,HouseRent,HouseSell,StoreRent,StoreSell
from estate.estate import Apartment,House,Store
from example import *

class ShowClient:

    ADVERTISEMENT_TYPES = {
        "ApartmentSell": ApartmentSell, "ApartmentRent": ApartmentRent,
        "HouseRent": HouseRent, "HouseSell": HouseSell,
         "StoreSell": StoreSell, "StoreRent": StoreRent
    }
    ADVERTISEMENT_TYPES_BROWSE = {
        1: ApartmentSell, 2: ApartmentRent,
        3: HouseRent, 4: HouseSell,
        5: StoreSell, 6: StoreRent
    }

    @staticmethod
    def show_all_properties():

        print("#"*25 + " all the properties " + "#"*25)
        for obj in ShowClient.ADVERTISEMENT_TYPES:
            print(f"{obj}:{ShowClient.ADVERTISEMENT_TYPES[obj].manager.count()}")
        print("#"*70 )

    @staticmethod
    def browse():
        user_input_browse = input("  0:exit\n  1:ApartmentSell\n  2:ApartmentRent\n  3:HouseRent\n  4:HouseSell\n"
                                      + "  5:StoreSell\n  6:StoreRent\n")
        if user_input_browse.isnumeric():
            user_input_browse=int(user_input_browse)
            if user_input_browse == 0:
                ShowClient.main()
            else:
                for choose in ShowClient.ADVERTISEMENT_TYPES_BROWSE:
                    if user_input_browse == choose:
                        for show_browse in ShowClient.ADVERTISEMENT_TYPES_BROWSE[choose].objects_list:
                            show_browse.show_detail()
                        ShowClient.browse()
                print("please choose valid number")
                ShowClient.browse()

    @staticmethod
    def add_properties():

        user_input_property = input("  0:exit\n  1:ApartmentSell\n  2:ApartmentRent\n  3:HouseRent\n  4:HouseSell\n"
                                      + "  5:StoreSell\n  6:StoreRent\n")
        if user_input_property.isnumeric():
            user_input_property=int(user_input_property)
            if user_input_property == 0:
                ShowClient.main()
            else:
                for choose in ShowClient.ADVERTISEMENT_TYPES_BROWSE:
                    if choose == user_input_property:

                        if choose == 1:
                            apartment_sell.insert_argument()
                            ShowClient.show_all_properties()

                        if choose == 2:
                            apartment_rent.insert_argument()
                            ShowClient.show_all_properties()

                        if choose == 3:
                            house_rent.insert_argument()
                            ShowClient.show_all_properties()
                        if choose == 4:
                            house_sell.insert_argument()
                            ShowClient.show_all_properties()
                        if choose == 5:
                            store_sell.insert_argument()
                            ShowClient.show_all_properties()

                        if choose == 6:
                            store_rent.insert_argument()
                            ShowClient.show_all_properties()
                        ShowClient.add_properties()
                print("please enter valid number")
                ShowClient.add_properties()

    @staticmethod
    def main():

            user_choose = input("\n"+ "for browsing in estate type '1' ,"
                                           "for adding estate type '2' ,"
                                           "for search in properties type '3' " + "\n")
            if user_choose.isnumeric():
                user_choose=int(user_choose)
                if user_choose == 1:

                    ShowClient.browse()

                if user_choose == 2:

                    ShowClient.add_properties()

                if user_choose == 3:
                    ShowClient.main()
            print("please enter valid number")
            ShowClient.main()

"""
x= ApartmentSell.manager.search(has_elevator=True)
print(len(x))
for i in x:
    pass
    #print(i.show_detail())
    
    x=inspect.signature(Rent.__init__)
z=[1,1,1,2,2,2,3,4,5,6,7,8,9,10]
zz=set(z)

for i in zz:
    print(i)
    
    
"""


ShowClient.show_all_properties()

ShowClient.main()

