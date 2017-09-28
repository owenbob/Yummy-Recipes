import re


class Recipes:
    def __init__(self, title, description, recipe_id):
        #method to initialize recipe attributes
        
        self.title = title
        self.description = description
        self.recipe_id = recipe_id
        self.recipe_items = {}
        self.new_recipe_items = {}
        self.done = []
        self.undone = []

    def create_recipe_items(self, new_item):
        #method to check if item id already exists
        
        if new_item.item_id in self.recipe_items.keys():
            return False
        elif new_item.title in self.new_recipe_items:
            return False

        else:
            self.recipe_items[new_item.item_id] = new_item
            self.new_recipe_items[new_item.item_id] = new_item.title
            return True

    def edit_recipe_item(self, title, quantity, price, status, item_id):
        #method to edit recipe item
        
        if item_id in self.recipe_items.keys():
            edit_recipe_item = self.recipe_items[item_id]
            edit_recipe_item.title = title
            edit_recipe_item.quantity = quantity
            edit_recipe_item.price = price
            edit_recipe_item.status = status
            return True
        return False

    def get_items(self):
        return self.recipe_items

    def get_item(self, item_id):
        if item_id in self.recipe_items.keys():
            return self.recipe_items[item_id]

    def del_item(self, item_id):
        #method to delete item
        
        if item_id in self.recipe_items.keys():
            del self.recipe_items[item_id]
            del self.new_recipe_items[item_id]
            return True
        return False
