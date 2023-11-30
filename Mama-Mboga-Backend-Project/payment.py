
class Payments:
    def __init__(self, order, method, amount):
        self.order = order
        self.method = method
        self.amount = amount

    def process_payment(self):
        print("Payment processing")

    def processed_payment(self):
        print("Payments processed")

payment1 = Payments(order="oranges", method="mpesa", amount=1000)
payment1.process_payment()

payment2 = Payments(order="kales", method="mpesa", amount=300)
payment3 = Payments(order="mangoes", method="account number", amount=200)
