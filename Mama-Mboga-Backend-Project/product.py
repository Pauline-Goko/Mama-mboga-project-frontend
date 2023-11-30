class Product:
    def __init__(self,name,price,category,stock):
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock
        
    def restock_product(self,amount):
        self.stock += amount
        print(self.stock)
        
    def sell(self,amount):
        if amount <= self.stock:
            self.stock -= amount
            print(f"{amount}  {self.name} are available")
        else:
            print(f"{self.name} is out of stock to sell {amount}")
            
    def view(self):
        print(f"Name:{self.name}")
        print(f"price:{self.price}")
        print(f"category:{self.category}")