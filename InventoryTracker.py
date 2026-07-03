class InventoryTracker:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity):
        self.inventory[item_name] = quantity

    def display_inventory(self):
        return self.inventory

    def checkStockLevel(self, item_name):
        if item_name in self.inventory:
            return self.inventory[item_name]
        return "Item not found"