# Class for inventory items
class InventoryItem:
    def __init__(self, name, current_stock, min_stock, unit):
        self.name = name
        self.current_stock = current_stock
        self.min_stock = min_stock
        self.unit = unit

    def is_low_stock(self):
        return self.current_stock <= self.min_stock