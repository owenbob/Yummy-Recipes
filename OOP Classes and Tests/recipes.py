"""
class contains functinality on how a user can interact with their recipes

"""

class Recipes(object):
    def __init__(self, title, description, recipe_id):
        #method to initialize list attributes
        
        self.title = title
        self.description = description
        self.recipe_id = recipe_id
