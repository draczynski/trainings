from datetime import datetime
from random import randint

# attributes are values attached to a class
#   - instance attributes - exist at instance level
#   - class attributes - exist at class definition level
#   - properties - attributes modified only from within the class

#   - instance methods - exists at instance level - needs an instance of class to be called
#   - static methods - exists at class def level - can be called directly from class

class Invoice:

    next_invoice_number = 1

    def __init__(self, payer, value):
        self.number = Invoice.next_invoice_number
        Invoice.next_invoice_number += 1

        self.payer = payer
        self.date = datetime.now()
        self.issued_by = "3M"
        self.items = []
        self.__secret_code = randint(1,100)
        self.value = value

    @staticmethod
    def validate_company_name_for_invoice(company_name):
        if company_name in ("HP", "Orlen", "Lotos"):
            print("Company Name is Valid!")
        else:
            print("NOT VALID")

    @property                        # this is a decorator
    def secret_code(self):           # this method name is the name we want the hidden attribute to be visible at
        return self.__secret_code    # here we use the hidden attribute name ("__attibutename")
    
    @secret_code.setter                         # this is a setter - special method used to change hidden value
    def secret_code(self, new_value):
        if 100 >= new_value >= 1:
            self.__secret_code = new_value
        else:
            print("Incorrect new value") 

    @secret_code.getter                         # this is a getter - special method used to access hidden value
    def secret_code(self):
        return "0000" + str(self.__secret_code)

    def __add__(self, other):
        return Invoice(f"{self.payer} & {other.payer}", self.value + other.value)

    def __repr__(self):
        return f"=======================\nInvoice number {self.number} for {self.payer}\nIssued on: {self.date}\n\nContains {len(self.items)} items\nTotal Value = {self.value}\n============================"

if __name__ == "__main__":
    inv1 = Invoice("HP", 100)
    inv2 = Invoice("Orlen", 2000)
    inv3 = Invoice("Lotos", 500)

    linked_invoice = inv1 + inv2 + inv3

    print(linked_invoice)

    Invoice.validate_company_name_for_invoice("Wedel")