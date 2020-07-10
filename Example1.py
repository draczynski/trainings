import os
from tkinter import messagebox


class Invoice:
    def __init__(self, name):
        self.__company_name = name
        self.items = []
    
    @classmethod
    def credit_note(cls, company_name):
        return cls("Credit Note for " + company_name)
    
    @staticmethod
    def validate_company_name(name):
        if name in ("3M", "HP", "Microsoft"):
            return True
        else:
            return False

    @property
    def company_name(self):
        return self.__company_name
    
    @company_name.setter
    def company_name(self, name):
        if self.validate_company_name(name):
            self.__company_name = name
        else:
            print(ValueError("Incorrect Company Name"))
    
    def add_item(self, item_name, price):
        self.items.append((item_name, price))
    
    @property
    def total_value(self):
        if self.items:
            return sum([int(item[1]) for item in self.items])
        else:
            return 0
    
    def __add__(self, other):
        inv = Invoice(self.company_name + " & " + other.company_name)
        for i in [self, other]:
            for item in i.items:
                inv.add_item(item[0], item[1])
        return inv

    def __repr__(self):
        return f"Invoice for company {self.company_name} for total amount of {self.total_value} $"

if __name__ == "__main__":
    inv1 = Invoice('3M')
    inv1.add_item("Laptop", 200)
    inv1.add_item("Tablet", 100)
    inv1.add_item("Office Chair", 300)


    inv2 = Invoice('HP')
    inv2.add_item("Paper", 50)

    inv3 = inv1 + inv2

    print(inv3.company_name, inv3.total_value)
    for item in inv3.items:
        print(item)

    print(inv3)
