from flask import *
from models.application import Application
from models.user import User
from models.recipes import Recipes
from models.recipe_Items import RecipeItems



app=Flask(__name__)

app.secret_key = 'owenbob101'
yummy_recipes = Application()  #Application object


# Rendering register page
@app.route("/")
@app.route("/register",methods=["GET", "POST"])
def register():
  
    #Route to enable user register on the site
    
    
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        

        if name and email and password:
            user = User(name, email, password)
            if yummy_recipes.register(user):
                flash('You have successfully registered')
                return redirect(url_for('login'))
            flash('User already exists') 
    return render_template("register.html")

# Rendering start pagewhich is the login page

@app.route("/login",methods=["GET", "POST"])
def login():
     #Route enables user to login after registration
   
   
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email and password:
            if yummy_recipes.login(email, password):
                session['email'] = email
                return redirect(url_for('dashboard'))
            flash ('Invalid credentials. Please try again')
            return render_template('login.html')
    return render_template('login.html')


# Rendering dashboard page page
@app.route("/dashboard",methods=["GET", "POST"])
def dashboard():
    
    #Route with the user profile user is able to see the number of recipes that they have
    
    user = yummy_recipes.get_user(session['email'])

    if not user:
        flash('You need to login first')
        return redirect(url_for('login'))
    recipes = user.total_recipes()
    return render_template("dashboard.html",user=user,recipes=recipes)


@app.route('/create/recipe')
def category():
    #route to create recipe
   
    error = None
    user = yummy_recipes.get_user(session['email'])
    if not user:
        flash('You need to login first')
        return redirect(url_for('login'))

    recipes = user.get_recipes()
    return render_template("category.html", recipes=recipes, error=error, user=user)
@app.route('/add/recipe', methods=['POST'])
def add_recipe():
   #Route to enable the user to create/add recipes
    

    user = yummy_recipes.get_user(session['email'])
    if not user:
        flash('You need to login first')
        return redirect(url_for('login'))
    recipes = user.get_recipes()
    title = request.form['title']
    description = request.form['description']

    if title and description:
        recipe_id = yummy_recipes.random_id()
        recipe1 = Recipes(title, description, recipe_id)

        
        if user.create_recipe(recipe1):
            flash('recipe successfully created')
            return redirect(url_for('category'))
        flash("recipe title already exists. Try again")
        
        return render_template('category.html', recipes=recipes, user=user)

    else:
        flash('You did not input a title or description. Try Again')
        return render_template('category.html', recipes=recipes, user=user)

@app.route('/edit/recipe/<recipe_id>', methods=['POST', 'GET'])
def edit_recipe(recipe_id):
    # route enables the user to check if they have any recipes
     
    user = yummy_recipes.get_user(session['email'])
    if not user:
        return redirect(url_for('login'))

    shop_recipe = user.get_recipe(recipe_id)
    if not shop_recipe:
        flash('recipe does not exist')
        return redirect(url_for('category'))

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        if title and description:
            if user.edit_recipe(recipe_id, title, description):
                flash('recipe successfully edited')
                return redirect(url_for('category'))
            flash('recipe not edited.')
            return render_template('edit_recipe.html', user=user, shop_recipe=shop_recipe)

        else:
            flash(" Please provide recipe title or description")
            return render_template('edit_recipe.html', user=user, shop_recipe=shop_recipe)

    return render_template('edit_recipe.html', user=user, shop_recipe=shop_recipe)


@app.route('/delete/recipe/<recipe_id>', methods=['GET', 'POST'])
def delete_recipe(recipe_id):
    """"
    This route enables the user to delete an existing recipe and all items items
    :param recipe_id
    """
    error = None
    user = yummy_recipes.get_user(session['email'])
    if not user:
        return redirect(url_for('login'))
    shop_recipe = user.get_recipe(recipe_id)
    if not shop_recipe:
        return redirect(url_for('category'))

    if request.method == 'POST':
        if user.del_recipe(recipe_id):
            flash("You have successfully deleted a recipe")
            return redirect(url_for('delete_recipe', recipe_id=shop_recipe.recipe_id))
        error = "Could not delete the Bucket"
    return render_template('delete_recipe.html', error=error, shop_recipe=shop_recipe, user=user)





@app.route('/add/recipe/item/<recipe_id>', methods=['POST', 'GET'])
def items(recipe_id):
    """"
    This route enables the users to create and view recipe items for specific recipes
    if no items have been created, some text is displayed
    :param recipe_id
    """
   
    user = yummy_recipes.get_user(session['email'])
    if not user:
        return redirect(url_for('login'))

    shop_recipe = user.get_recipe(recipe_id)
    if not shop_recipe:
        return redirect(url_for('category'))

    return render_template('items.html', user=user, shop_recipe=shop_recipe)

@app.route('/delete/recipe/item/<recipe_id>/<item_id>', methods=['GET', 'POST'])
def delete_item(recipe_id, item_id):
    """"
    This route enables the user to delete any of the items
    :param recipe_id
    :param item_id
    """
    error = None
    user = yummy_recipes.get_user(session['email'])
    if not user:
        return redirect(url_for('login'))

    shop_recipe = user.get_recipe(recipe_id)
    item = shop_recipe.get_item(item_id)
    if not shop_recipe and not item:
        flash('Item does not exist')
        return redirect(url_for('items', recipe_id=recipe_id))

    if request.method == 'POST':
        if shop_recipe.del_item(item_id):
            flash('Item has been deleted')
            return redirect(url_for('items', recipe_id=shop_recipe.recipe_id))

        error = 'Item was not deleted'
    return render_template('delete_items.html', error=error, user=user, shop_recipe=shop_recipe, item=item)

@app.route('/logout')
def logout():
    """"
    route to log out user
    """
    session.pop('email', None)
    flash('You have been logged out')
    return redirect(url_for('login'))




if __name__ == "__main__":
    app.run(debug=True)
