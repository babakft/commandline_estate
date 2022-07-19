from estate.sellerInformation import SellerInformation
from deal.deal_type import Rent,Sell
from deal.advertisment import ApartmentSell,ApartmentRent,HouseRent,HouseSell,StoreRent,StoreSell
from estate.estate import Apartment,House,Store
from example import example

class ShowClient:

    ADVERTISEMENT_TYPES = {
        "ApartmentSell": ApartmentSell, "ApartmentRent": ApartmentRent,
        "HouseRent": HouseRent, "HouseSell": HouseSell,
        # 5: StoreSell, 6: StoreRent
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
        user_input_browse = int(input("  0:exit\n  1:ApartmentSell\n  2:ApartmentRent\n  3:HouseRent\n  4:HouseSell\n"
                                      + "  5:StoreSell\n  6:StoreRent\n"))
        if user_input_browse ==0:
            return
        else:
            for choose in ShowClient.ADVERTISEMENT_TYPES_BROWSE:
                if user_input_browse == choose:
                    for show_browse in ShowClient.ADVERTISEMENT_TYPES_BROWSE[choose].objects_list:
                        show_browse.show_detail()
                    ShowClient.browse()
            print("1 please choose valid number")
            ShowClient.browse()

    @staticmethod
    def main():

            user_choose = int(input("\n"+ "for browsing in estate type '1' ,"
                                           "for adding estate type '2' ,"
                                           "for search in properties type '3' " + "\n"))

            if user_choose == 1:

                ShowClient.browse()

            if user_choose == 2:
                pass

            if user_choose == 3:
                pass


            ShowClient.main()


example()
"""
x= ApartmentSell.manager.search(has_elevator=True)
print(len(x))
for i in x:
    pass
    #print(i.show_detail())
"""


ShowClient.show_all_properties()

ShowClient.main()