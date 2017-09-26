"""
User class that should contain our functions  and variables for testing
"""

class User(object):

    #A user should  contain a username,email address and a password in order to use Yummy recipes
    
    def __init__(self,username,email,password):
        #Initiliazing the values of username ,email and password

        self.username = username
        self.email = email
        self.password = password
