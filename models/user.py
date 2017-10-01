import re


class User:
    def __init__(self, username, email, password):
        
    # method to initialize user attributes
        
        self.username = username
        self.email = email
        self.password = password
        self.recipes = {}
        self.new_recipes = {}
        # self.recipe_items = {}

    def create_recipe(self, recipe1):
        
        #method to check if the recipe id exists
        
        if recipe1.recipe_id in self.recipes.keys():
            return False
        elif recipe1.title in self.new_recipes:
            return False

        else:
            self.recipes[recipe1.recipe_id] = recipe1
            self.new_recipes[recipe1.recipe_id] = recipe1.title
            return True

    def total_recipes(self):
        
        #method to return the total number of recipes created
        
        return len(self.recipes)

    def edit_recipe(self, recipe_id, title, description):
        #method to edit the title of an existing bucket recipe
        
        if recipe_id in self.recipes.keys():
            edited_recipe = self.recipes[recipe_id]
            edited_recipe.title = title
            edited_recipe.description = description
            return True
        return False

    def get_recipes(self):       
        #method to get all recipes that have been created
        
        return self.recipes

    def get_recipe(self, recipe_id):     
        #method to get single recipe using recipe id
        
        if recipe_id in self.recipes.keys():
            return self.recipes[recipe_id]
        return None

    def del_recipe(self, recipe_id):
        #method to delete recipe
        
        if recipe_id in self.recipes.keys():
            del self.recipes[recipe_id]
            del self.new_recipes[recipe_id]
            return True
        return None
