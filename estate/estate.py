from abc import ABC,abstractmethod


class Estate(ABC):
    def __init__(self,seller_information,area,room_count,build_year,region,address,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.seller_information=seller_information
        self.area=area
        self.room_count=room_count
        self.build_year=build_year
        self.region=region
        self.address=address


    @abstractmethod
    def show_description(self):
       pass

    def show_estate_description(self):
        print( f"seller_information = {self.seller_information}\n\n"
        f"room_count = {self.room_count}\t area ={self.area}\t"
        f"build_year ={self.build_year}\n"
        f"region ={self.region}\t address ={self.address}")


class Apartment(Estate):
    def __init__(self,has_elevator,has_parking,floor,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.has_elevator=has_elevator
        self.has_parking=has_parking
        self.floor=floor

    def show_description(self):
        self.show_estate_description()
        print(f"has_elevator ={self.has_elevator}\t has_parking ={self.has_parking}\t floor ={self.floor}")


class House(Estate):
    def __init__(self,has_yard,floor,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.has_yard=has_yard
        self.floor=floor


    def show_description(self):
        self.show_estate_description()
        print(f"has_yard ={self.has_yard}\t floor ={self.floor}")

class Store(Estate):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)


    def show_description(self):
        self.show_estate_description()