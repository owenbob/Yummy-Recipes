import unittest



from Classes.user import User
from Classes.recipes import Recipes

"""
Class below to test if user can create ,view ,update and delete lists
    -Also should keep
"""
class userTestCase(unittest.TestCase):

    def setUp(self):
        self.user = User("spiderman", "spiderman@gmail.com", "maryJaneparker")
        self.new_recipe=Recipes("Rolex recipe","Obtain ingredients - eggs and chapatis","546")

    #Test if the user has Username Variable
    def test_username(self):
        self.assertEqual(self.user.username, "spiderman", msg = "Username is invalid")

    #Test if the user has Email Variable
    def test_emailaddress(self):
        self.assertEqual(self.user.email, "spiderman@gmail.com", msg = "Email is Invalid")

    #Test if the user has Password Variable
    def test_password(self):
        self.assertEqual(self.user.password, "maryJaneparker", msg = "Password is invaid")

    #Test if the User can be registered
    def test_registerUser(self):
        self.user.registerUser(["spiderman", "spiderman@gmail.com", "maryJaneparker"])
        self.assertEqual(self.user.database, [["spiderman", "spiderman@gmail.com", "maryJaneparker"]], msg="User Not Registered")

    #Test Import of Recipes class to make sure the user can interact with a recipe
    def test_recipe_class(self):
        self.assertIsInstance(self.new_recipe,Recipes, msg='Object is not an instance of the  class')
        
    #Test if user can create a recipe
    def test_create_recipe(self):
            self.assertTrue(self.user.create_recipe(self.new_recipe))
    
    def test_recipe_to_create_already_exists(self):
        recipe1 = Recipes("Rolex recipe","Obtain ingredients - eggs and chapatis","546")
        self.user.recipes = {"546": recipe1}
        self.assertFalse(self.user.create_recipe(recipe1))
    
    def test_new_recipe_stored_in_dictionary(self):
        self.assertEqual(type(self.user.get_recipes()), dict, msg='Output is not a dictionary')
    

    def test_a_recipe_is_returned_when_an_id_is_specified(self):
        recipe1 = Recipes("Rolex recipe","Obtain ingredients - eggs and chapatis","546")
        self.user.recipes = {"546": recipe1}
        self.assertEqual(self.user.get_recipe("546"), recipe1)

    def test_none_is_returned_for_recipe_doesnot_exist(self):
        self.assertIsNone(self.user.get_recipe("Sandwich"))

    def test_edit_recipe(self):
        self.user.create_recipe(self.new_recipe)
        self.assertTrue(self.user.edit_recipe("Sandwich","Obtain ingredients-bread ,salads,bacon" ,"546"))

    def test_recipe_to_edit_doesnt_exists(self):
        recipe1 = Recipes("Rolex recipe","Obtain ingredients - eggs and chapatis","546")
        self.user.create_recipe(recipe1)
        self.assertFalse(self.user.edit_recipe("Sandwich","Obtain ingredients-bread ,salads,bacon" ,"548"))

    def test_del_recipe(self):
        self.user.create_recipe(self.new_recipe)
        self.assertTrue(self.user.del_recipe("546"))

    def test_recipe_to_delete_doesnt_exists(self):
        recipe1 = Recipes("Rolex recipe","Obtain ingredients - eggs and chapatis","546")
        self.user.create_recipe(recipe1)
        self.assertFalse(self.user.del_recipe("548"))

  
