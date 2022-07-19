from base.baseclass import BaseClass

class SellerInformation(BaseClass):

    def __init__(self, first_name, last_name, number):
        super().__init__()
        self.name=first_name
        self.lastname=last_name
        self.number=number

    def __str__(self):
       return f"{self.name} {self.lastname}   number:{self.number}"
