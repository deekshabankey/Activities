"""
Write a Python class,

MedPlus, that has three instance variables of type str, int, and float, that respectively represent the name of the medicine, batch number, and its price.

Your class must include a constructor method that initializes each variable to an appropriate value, and your class should include methods for setting the value of each type, and retrieving the value of each type

If the user passes invalid parameters to the constructor method in that case raise an appropriate error to the user of your class
"""
#basic class
class Medplus:
    def __init__(self,name:str,batch:int,price:float):
        self.name=name
        self.batch=batch
        self.price=price
    def s_name(self,name:str):
        self.name = name
        return self.name
    def s_batch(self,batch:int):
        self.batch=batch
        return self.batch
    def s_price(self,price:float):
        self.price=price
        return self.price
    def get_name(self)->str:
        return self.name
    def get_batch(self)->float:
        return self.batch
    def get_price(self)->int:
        return self.price
    
a=Medplus("Paracetamol",21,15.5)
print(a.s_name('Dolo'))
print(a.s_price(23))
