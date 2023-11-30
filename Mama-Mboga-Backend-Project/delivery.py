# class Order:
#     def __init__(self, deliveryOptions):
#         self.deliveryOptions = deliveryOptions
#     def getDeliveryOptions(self):
#         return self.deliveryOptions
# order = Order( [ "Home Delivery", "Pickup point"])
# deliveryOptions = order.getDeliveryOptions()
# print(deliveryOptions)




class Shipment:
    def __init__(self, date,order, location, delivery_options, delivery_type, shipment_cost, status, delivery_time):
        self.date = date
        self.order = order
        self.location = location
        self.delivery_options = delivery_options
        self.delivery_type = delivery_type
        self.shipment_cost = shipment_cost
        self.status = status
        self.delivery_time = delivery_time

    def change_delivery_date(self, new_date):
        self.date = new_date

    def change_delivery_methods(self, new_delivery_options, new_delivery_type):
        self.delivery_options = new_delivery_options
        self.delivery_type = new_delivery_type

    def change_status(self, new_status):
        self.status = new_status

    def pay(self, payment_amount):
        print(f"Payment of {payment_amount} received for the shipment.")

    def display_shipment_details(self):
        print("Shipment Details:")
        print(f"Date: {self.date}")
        print(f"Order: {self.order}")
        print(f"Location: {self.location}")
        print(f"Delivery Options: {self.delivery_options}")
        print(f"Delivery Type: {self.delivery_type}")
        print(f"Shipment Cost: {self.shipment_cost}")
        print(f"Status: {self.status}")
        print(f"Delivery Time: {self.delivery_time}")



# Creating a shipment
shipment1 = Shipment("Apples", "Nairobi", "Home", "Person", 150, "Processing", "1 day")
shipment1.display_shipment_details()

# Changing the delivery date
shipment1.change_delivery_date("2023-05-30")

# Changing delivery methods
shipment1.change_delivery_methods("Pick up point", "Motorbike")

# Changing status
shipment1.change_status("Shipped")

# Making a payment
shipment1.pay(650)

# Displaying updated shipment details
shipment1.display_shipment_details()
