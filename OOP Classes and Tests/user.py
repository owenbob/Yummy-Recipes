"""
User class that should contain our functions  and variables for testing
the database list belongs to the app as a databse
"""

class User(object):

    #A user should  contain a username,email address and a password in order to use Yummy recipes
    
    def __init__(self,username,email,password):
        #Initiliazing the values of username ,email and password

        self.username = username
        self.email = email
        self.password = password
        self.database = []
        self.recipes = {}
        self.new_recipes = {}

    def registerUser(self,list):
        self.database.append(list)
        return self.database

    def create_recipe(self, recipe1):
        #method to check if the list id exists if not,  create a new list
        
        if recipe1.recipe_id in self.recipes.keys():
            return False
        elif recipe1.title in self.new_recipes:
            return False

        else:
            self.recipes[recipe1.recipe_id] = recipe1
            self.new_recipes[recipe1.recipe_id] = recipe1.title
            return True

    def get_recipes(self):
        #method to get all lists that have been created
        
        return self.recipes

    def get_recipe(self, recipe_id):
        #method to get single list using list id
        
        if recipe_id in self.recipes.keys():
            return self.recipes[recipe_id]
        return None
    def edit_recipe(self,  title, description,recipe_id):
      
        #method to edit the title  and description of an existing recipe 
        
        if recipe_id in self.recipes.keys():
            edited_recipe = self.recipes[recipe_id]
            edited_recipe.title = title
            edited_recipe.description = description
            return True
        return False

    def del_recipe(self, recipe_id):
        #method to delete list
        
        if recipe_id in self.recipes.keys():
            del self.recipes[recipe_id]
            del self.new_recipes[recipe_id]
            return True
        return None


