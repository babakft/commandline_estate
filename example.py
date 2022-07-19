from estate.sellerInformation import SellerInformation
from deal.deal_type import Rent,Sell
from deal.advertisment import ApartmentSell,ApartmentRent,HouseRent,HouseSell,StoreRent,StoreSell
from estate.estate import Apartment,House,Store


def example():
    a = SellerInformation("ali", "aa", 123)
    b = SellerInformation("babak", "bb", 456)
    c = SellerInformation("behnam", "cc", 789)

    print(SellerInformation.objects_list[1])

    apartment = Apartment(
        has_elevator=True, has_parking=True, floor=2, seller_information=SellerInformation.objects_list[0],
        build_year=1393, region="reg1", area=80, room_count=2,
        address="Some text..."
    )

    house = House(
        has_yard=True, floor=1, seller_information=SellerInformation.objects_list[2], area=400,
        room_count=6, build_year=1370, region="reg1", address='Some text ...'
    )

    store = Store(
        seller_information=SellerInformation.objects_list[2], area=30, room_count=0, build_year=1390,
        region="reg1", address="Some text ...."
    )


    apartment_sell = ApartmentSell(has_elevator=True, has_parking=False, floor=2
                                   , seller_information=SellerInformation.objects_list[1],
                                   area=50, room_count=20, build_year=1234, region="reg1",
                                   address="blab", price_per_meter=5, discount=True, convert_able=False)
    apartment_sell1 = ApartmentSell(has_elevator=True, has_parking=False, floor=2
                                   , seller_information=SellerInformation.objects_list[1],
                                   area=50, room_count=20, build_year=1234, region="reg1",
                                   address="blab", price_per_meter=5, discount=True, convert_able=False)
    apartment_sell2 = ApartmentSell(has_elevator=True, has_parking=False, floor=2
                                   , seller_information=SellerInformation.objects_list[1],
                                   area=50, room_count=20, build_year=1234, region="reg1",
                                   address="blab", price_per_meter=5, discount=True, convert_able=False)

    apartment_rent = ApartmentRent(
        has_elevator=True, has_parking=True, floor=2, seller_information=SellerInformation.objects_list[0],
        build_year=1393, region="reg1", area=80, room_count=2,
        initial_price=100, rent_price=3.5, address="Some text...", discount=True
    )

    house_rent = HouseRent(
        has_yard=True, floor=1, seller_information=SellerInformation.objects_list[2], area=400,
        room_count=6, build_year=1370, region="reg1", address='Some text ...',
        initial_price=100, rent_price=3.5, discount=True
    )

    house_sell = HouseSell(
        has_yard=True, floor=1, seller_information=SellerInformation.objects_list[0], area=400,
        room_count=6, build_year=1370, region="reg1", address='Some text ...',
        price_per_meter=20, discount=True, convert_able=False
    )

    store_sell = StoreSell(seller_information=SellerInformation.objects_list[1]
                           , area=10, room_count=2, build_year=1997, region="azadi", address="amirkabir",
                           price_per_meter=15, discount=False, convert_able=True
                           )

    store_rent = StoreRent(seller_information=SellerInformation.objects_list[1]
                           , area=10, room_count=2, build_year=1997, region="azadi", address="amirkabir",
                           initial_price=800, rent_price=150, discount=True)

