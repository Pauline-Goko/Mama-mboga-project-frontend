# customer
class Customer:
    def __init__(self,name,phone_number,email,address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.cart = []
#I have created an empty list so the customer can be able to append to the empty list every time they
#purchase goods
    def add_to_cart(self,*item):
        self.cart.append(item)
        print(self.cart)
    def remove_from_cart(self,item):
        if item in self.cart:
            self.cart.remove(item)
            print(self.cart)