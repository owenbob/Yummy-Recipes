class recipeItems(object):
    #Recipe items class
   
    #Method to create Initial listof recipe items and Read What it contains
    def __init__(self,lst=None):
        self.lst = lst or []
    #Method to add recipe item list
    def add_to_recipe_item_list(self,item):
        self.lst.append(item)
        return self.lst
    #Method to update recipe item with new item
    def update_recipe_item_list_with_new_item(self,item):
        self.lst.append(item)
        return self.lst
    
        
        
