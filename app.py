from flask import Flask, render_template, request, redirect		# gets flask and templates
import utils.ingredientDatabase
app = Flask(__name__) # Creates a web page

@app.route("/") # when someone goes to "/"
def index():
	return render_template("index.html") # show this

@app.route("/ingredient-maker")
def ingredientMaker():
	return render_template("ingredient-maker.html")


@app.route("/submitMakeIngredient", methods=['POST'])
def handleData():
	ingredientName = request.form['ingredient-name']
	calories = int(request.form.get('calories'))
	protein = int(request.form.get('protein'))
	carbs = int(request.form.get('carbs'))
	fats = int(request.form.get('fats'))
	utils.ingredientDatabase.main(
		ingredientName,calories,protein,carbs,fats)
	return f"<h1>Thank you for submitting {ingredientName}</h1>"

@app.route("/delete-ingredients", methods=['POST'])
def deletetables():
	utils.ingredientDatabase.deleteTable()
	return render_template("index.html")





if __name__ == "__main__":
	app.run(debug="true")  # starts website