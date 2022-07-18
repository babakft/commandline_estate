from abc import ABC

class Sell(ABC):
    def __init__(self,price_per_meter,discount,convert_able):
        self.price_per_meter=price_per_meter
        self.discount=discount
        self.convert_able=convert_able


class Rent(ABC):
    def __init__(self,initial_price,rent_price,discount):
        self.initial_price=initial_price
        self.rent_price=rent_price
        self.discount=discount


