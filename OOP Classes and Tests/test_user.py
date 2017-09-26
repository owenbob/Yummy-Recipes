import unittest

from user import User

"""
Class below to test if user can create ,view ,update and delete lists
    -Also should keep
"""
class userTestCase(unittest.TestCase):

    def setUp(self):
        self.user = User("spiderman", "spiderman@gmail.com", "maryJaneparker")

    #Test is the user has Username Variable
    def test_username(self):
        self.assertEqual(self.user.username, "spiderman", msg = "Username is invalid")

        #Test is the user has Username Variable
    def test_emailaddress(self):
        self.assertEqual(self.user.email, "spiderman@gmail.com", msg = "Email is Invalid")

    #Test is the user has Username Variable
    def test_password(self):
        self.assertEqual(self.user.password, "maryJaneparker", msg = "Password is invaid")
