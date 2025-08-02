import sqlite3
from utils.loginDatabase import *
ingredients = []



def deleteTable(): #simply deletes the tables (dev)
	with sqlite3.connect('database.db') as conn:
		cursor_obj = conn.cursor() 
		cursor_obj.execute("""DROP TABLE IF EXISTS ingredients""")


def createTable(): #creates a table for ingredients if not exists , eg first time opening it
	with sqlite3.connect('database.db') as conn:
		cursor_obj = conn.cursor() 
		ingredientTable = """CREATE TABLE IF NOT EXISTS ingredients ( 
										ingredientName TEXT NOT NULL PRIMARY KEY,
										Calories INT NOT NULL,
										Protien INT ,
										Carbs INT,
										Fats INT
										)
								"""
		cursor_obj.execute(ingredientTable) #creates


def storeIngredients(ingredientname,cal,pro,car,fat): #takes variable from app.py (hopefully)
	with sqlite3.connect('database.db') as conn:
		cursor_obj = conn.cursor() 
		cursor_obj.execute(""" INSERT OR IGNORE INTO ingredients
											(ingredientName,Calories,Protien,Carbs,Fats) VALUES 	(?,?,?,?,?)
									""", (ingredientname,cal,pro,car,fat)) #inserts variables


def deleteIngredient():
	pass



def checkForTable():
	with sqlite3.connect('database.db') as conn:
		cursor_obj = conn.cursor()
		cursor_obj.execute("""
										 SELECT name FROM sqlite_master
										 WHERE type ='table' and name ='ingredients';
										 """)
		tableExists = cursor_obj.fetchone()

		if tableExists:
			return True
		else:
			return False

def main(name,cal,pro,car,fat):
	if checkForTable():
		storeIngredients(name,cal,pro,car,fat)
		print("table existed")
	else:
		createTable()
		storeIngredients(name,cal,pro,car,fat)
		print("table had to be created")
