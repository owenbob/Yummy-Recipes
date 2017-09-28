import unittest

from recipeItem import recipeItems

"""
Test class for Receipes and RecipeItem Classes
Looking at CRUD(Create,Read,Update and Delete) functionality on Recipes
Testing also if the Recipe Items can be edited
"""

class testRecipesTestCase(unittest.TestCase):
    #Class to test create, edit, view and delete bucket items.

    def setUp(self):
            self.itemslist = recipeItems()

        #test to see if recipe item List has been created
    def test_recipelist(self):
        self.assertEqual(self.itemslist.lst,[],msg =" recipe Item list has not been created")

         #Test for add item to an empty recipe item list
    def test_add_to_recipe_item_list(self):
        self.itemslist.add_to_recipe_item_list('obtain ingredients')
        self.assertEqual(self.itemslist.lst, ['obtain ingredients'], msg=" recipe Item list has not been updated with new item")

        #Test for updating list with a new item
    def test_update_recipe_item_with_new_item(self):
        self.itemslist.add_to_recipe_item_list('cook for twenty minutes')
        self.assertEqual(self.itemslist.lst, ['cook for twenty minutes'], msg=" recipe Item list has not been updated with new item")

    
   
        