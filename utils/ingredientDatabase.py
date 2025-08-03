import sqlite3
from utils.loginDatabase import *


def deleteTable(): #simply deletes the tables (dev)
	with sqlite3.connect('database.db') as conn:
		cursor_obj = conn.cursor() 
		cursor_obj.execute("""DROP TABLE IF EXISTS ingredients""")


def createTables():  # creates tables if not exist
    with sqlite3.connect('database.db') as conn:
        cursor_obj = conn.cursor()

        ingredientTable = """
        CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            Calories INT NOT NULL,
            Protein INT,
            Carbs INT,
            Fats INT
        )
        """

        mealTable = """
        CREATE TABLE IF NOT EXISTS meals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            Calories INT NOT NULL,
            Protein INT,
            Carbs INT,
            Fats INT
        )
        """

        meal_ingredients_table = """
        CREATE TABLE IF NOT EXISTS junction (
            meal_id INTEGER,
            ingredient_id INTEGER,
            quantity REAL,
            PRIMARY KEY (meal_id, ingredient_id),
            FOREIGN KEY (meal_id) REFERENCES meals(id),
            FOREIGN KEY (ingredient_id) REFERENCES ingredients(id)
        )
        """

        cursor_obj.execute(ingredientTable)
        cursor_obj.execute(mealTable)
        cursor_obj.execute(meal_ingredients_table)
        conn.commit()

def storeIngredients(name,cal,pro,car,fat): #takes variable from app.py (hopefully)
	with sqlite3.connect('database.db') as conn:
		cursor_obj = conn.cursor() 
		cursor_obj.execute(""" INSERT OR IGNORE INTO ingredients
											(name,Calories,Protein,Carbs,Fats) VALUES 	(?,?,?,?,?)
									""", (name,cal,pro,car,fat)) #inserts variables


def deleteIngredient():
	pass



def checkForTables():
	with sqlite3.connect('database.db') as conn:
		cursor_obj = conn.cursor()
		cursor_obj.execute("""
										 SELECT name FROM sqlite_master
										 WHERE type ='table' and name ='ingredients';
										 """)
		ingredientTableExists = cursor_obj.fetchone()
		cursor_obj.execute("""
										 SELECT name FROM sqlite_master
										 WHERE type ='table' and name ='meals';
										 """)
		mealsTableExists = cursor_obj.fetchone()
		cursor_obj.execute("""
										 SELECT name FROM sqlite_master
										 WHERE type ='table' and name ='junction';
										 """)
		junctionTableExists = cursor_obj.fetchone()

		if ingredientTableExists and mealsTableExists and junctionTableExists:
			return True
		else:
			return False

def get_all_ingredients():
	with sqlite3.connect('database.db') as conn:
		cursor_obj = conn.cursor()
		cursor_obj.execute("""SELECT id, name FROM ingredients""")
		rows = cursor_obj.fetchall()
		return rows



def main(name,cal,pro,car,fat):
	if checkForTables():
		storeIngredients(name,cal,pro,car,fat)
		print("table existed")
	else:
		createTables()
		storeIngredients(name,cal,pro,car,fat)
		print("table had to be created")
