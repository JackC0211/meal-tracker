from flask import Flask, render_template, request, redirect		# gets flask and templates
import utils.mealsDatabase 
app = Flask(__name__) # Creates a web page

















@app.route("/") # when someone goes to "/"
def index():
	return render_template("index.html") # show this

@app.route( "/meal-maker", methods=['GET','POST'] ) #when someone goes to "/about"
def mealMaker():
	return render_template("meal-maker.html")


@app.route("/submitMakeMeal", methods=['POST'])
def handleData():
	mealName = request.form.get('meal-name')
	calories = request.form.get('calories')
	protein = request.form.get('protein')
	carbs = request.form.get('carbs')
	fats = request.form.get('fats')
	utils.mealsDatabase.storeMeals(
		mealName,calories,protein,carbs,fats)
	return f"<h1>Thank you for submitting {mealName}</h1>"








if __name__ == "__main__":
	app.run(debug="true")  # starts website