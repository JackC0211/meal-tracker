from flask import Flask, render_template		# gets flask and templates

app = Flask(__name__) # Creates a web page

@app.route("/") # when someone goes to "/"
def index():
	return render_template("index.html") # show this

@app.route("/about") #when someone goes to "/about"
def about():
	return render_template("about.html")

if __name__ == "__main__":
	app.run(debug="true")  # starts website