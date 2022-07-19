from abc import ABC

class Sell(ABC):
    def __init__(self,price_per_meter,discount,convert_able,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.price_per_meter=price_per_meter
        self.discount=discount
        self.convert_able=convert_able


    def show_deal(self):
        print(f"\nprice_per_meter ={self.price_per_meter}\t discount ={self.discount}\t "
              f"convert_able ={self.convert_able}\t")

class Rent(ABC):
    def __init__(self,initial_price,rent_price,discount,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.initial_price=initial_price
        self.rent_price=rent_price
        self.discount=discount


    def show_deal(self):
        print(f"\ninitial_price ={self.initial_price}\t rent_price ={self.rent_price}\t"
              f"discount ={self.discount}\t")
