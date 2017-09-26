"""
class contains functinality on how a user can interact with their recipes
"""

class Recipes(object):


    def __init__(self, title, description, recipe_id):
        #Initilizing the recipe parameters
        self.title = title
        self.description = description
        self.recipe_id = recipe_id
        self.recipe_items = {}
        self.new_recipe_items = {}