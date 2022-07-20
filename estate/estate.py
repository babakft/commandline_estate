import inspect
from abc import ABC,abstractmethod

"""
this file is use just for inheritance and it's base for method that use in advertisement
"""
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
        print(f"seller_information = {self.seller_information}\n\n"
              f"room_count = {self.room_count}\t area ={self.area}\t"
              f"build_year ={self.build_year}\n"
              f"region ={self.region}\t address ={self.address}")
    @abstractmethod
    def show_argument(self):
        pass
    @staticmethod
    def show_estate_argument():
        argument=set()
        for arg in inspect.signature(Estate.__init__).parameters.values():
            argument.add(arg)
        return argument




class Apartment(Estate):
    def __init__(self,has_elevator,has_parking,floor,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.has_elevator=has_elevator
        self.has_parking=has_parking
        self.floor=floor

    def show_description(self):
        self.show_estate_description()
        print(f"has_elevator ={self.has_elevator}\t has_parking ={self.has_parking}\t floor ={self.floor}")

    def show_argument(self):
       arg_estate= self.show_estate_argument()
       arg_apartment=set()
       for arg in inspect.signature(Apartment.__init__).parameters.values():
           arg_apartment.add(arg)
       return arg_estate.union(arg_apartment)

class House(Estate):
    def __init__(self,has_yard,floor,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.has_yard=has_yard
        self.floor=floor


    def show_description(self):
        self.show_estate_description()
        print(f"has_yard ={self.has_yard}\t floor ={self.floor}")

    def show_argument(self):
        arg_estate = self.show_estate_argument()
        arg_house = set()
        for arg in inspect.signature(House.__init__).parameters.values():
            arg_house.add(arg)
        return arg_estate.union(arg_house)

class Store(Estate):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_description(self):
        self.show_estate_description()

    def show_argument(self):
        arg_estate = self.show_estate_argument()
        arg_store= set()
        for arg in inspect.signature(Store.__init__).parameters.values():
            arg_store.add(arg)
        return arg_estate.union(arg_store)