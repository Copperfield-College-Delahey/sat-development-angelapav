#Class for orders
class Order:
    def __init__(self, name, email, item, quantity, deadline):
        self.name = name 
        self.email = email
        self.item = item
        self.quantity = quantity
        self.deadline = deadline
        self.done= False