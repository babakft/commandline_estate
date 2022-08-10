from example import store_rent, store_sell, house_sell, house_rent, apartment_rent,\
    apartment_sell, ApartmentSell
from example import ApartmentRent, HouseRent, HouseSell, StoreRent, StoreSell


class ShowClient:
    """
    a class that show in command line in here we have search,browse,insert
    """
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
        """
        show every class list_object
        """
        print("#"*25 + " all the properties " + "#"*25)
        for obj in ShowClient.ADVERTISEMENT_TYPES:
            print(f"{obj}:{ShowClient.ADVERTISEMENT_TYPES[obj].manager.count()}")
        print("#" * 70)

    @staticmethod
    def browse():

        """
           use show detail method in advertisement.py
           and use it to show all property information
        """

        user_input_browse = input("  0:exit\n  1:ApartmentSell\n  2:ApartmentRent\n  3:HouseRent\n  4:HouseSell\n"
                                  + "  5:StoreSell\n  6:StoreRent\n")

        if user_input_browse.isnumeric():
            user_input_browse = int(user_input_browse)
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

        """
                  method for insert new obj
                  it uses one instance to get needed argument
                  than use for loop to get needed argument => insert_argument()

        """

        user_input_property = input("0:exit\n  1:ApartmentSell\n  2:ApartmentRent\n  3:HouseRent\n  4:HouseSell\n"
                                    + "  5:StoreSell\n  6:StoreRent\n")
        if user_input_property.isnumeric():
            user_input_property = int(user_input_property)
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
    def search():

        """
           use base. search to search
        """

        user_search_input = input("  0:exit\n  1:search by region\n  2:search by area\n  3:search by room_count\n")
        result = list()

        def search_by(**kwargs):
            for obj in ShowClient.ADVERTISEMENT_TYPES_BROWSE.values():
                search_result = obj.manager.search(**kwargs)
                result.extend(search_result)
            if len(result) != 0:
                for i in result:
                    i.show_detail()
            else:
                print("noting in properties")

        if user_search_input.isnumeric():
            user_search_input = int(user_search_input)
            if user_search_input == 0:
                ShowClient.main()
            else:
                if user_search_input == 1:
                    base = input("please enter region \n")
                    search_by(region=base)
                if user_search_input == 2:
                    base = input("please enter area \n")
                    if base.isnumeric():
                        base = int(base)
                    search_by(area=base)
                if user_search_input == 3:
                    base = input("please enter room_count \n")
                    if base.isnumeric():
                        base = int(base)
                    search_by(room_count=base)
                ShowClient.search()
        print("please enter valid number")
        ShowClient.search()

    @staticmethod
    def main():

        user_choose = input("\n" + "for browsing in estate type '1' ,"
                            "for adding estate type '2' ,"
                            "for search in properties type '3' " + "\n")

        if user_choose.isnumeric():
            user_choose = int(user_choose)
            if user_choose == 1:

                ShowClient.browse()

            if user_choose == 2:

                ShowClient.add_properties()

            if user_choose == 3:
                ShowClient.search()
            print("please enter valid number")
            ShowClient.main()


ShowClient.show_all_properties()
ShowClient.main()
