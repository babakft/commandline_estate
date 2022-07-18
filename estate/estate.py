from abc import ABC,abstractmethod


class Estate(ABC):
    def __init__(self,seller_information,area,room_count,build_year,region,address):
        self.seller_information=seller_information
        self.area=area
        self.room_count=room_count
        self.build_year=build_year
        self.region=region
        self.address=address

    @abstractmethod
    def show_description(self):
            pass


class Apartment(Estate):
    def __init__(self,has_elevator,has_parking,floor_count,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.has_elevator=has_elevator
        self.has_parking=has_parking
        self.floor_count=floor_count

    def show_description(self):
            pass


class House(Estate):
    def __init__(self,has_yard,floor_count,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.has_yard=has_yard
        self.floor_count=floor_count


    def show_description(self):
        pass


class Store(Estate):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)


    def show_description(self):
        pass
