import sqlite3
from utils.loginDatabase import *
meals = []



def deleteTable(): #simply deletes the tables (dev)
	with sqlite3.connect('meals.db') as conn:
		cursor_obj = conn.cursor() 
		cursor_obj.execute("""DROP TABLE IF EXISTS meals""")


def createTable(): #creates a table for meals if not exists , eg first time opening it
	with sqlite3.connect('meals.db') as conn:
		cursor_obj = conn.cursor() 
		mealsTable = """CREATE TABLE IF NOT EXISTS meals ( 
										mealName TEXT PRIMARY KEY,
										Calories INT NOT NULL,
										Protien INT ,
										Carbs INT,
										Fats INT
										)
								"""
		cursor_obj.execute(mealsTable) #creates


def storeMeals(name,cal,pro,car,fat): #takes variable from app.py (hopefully)
	with sqlite3.connect('meals.db') as conn:
		cursor_obj = conn.cursor() 
		cursor_obj.execute(""" INSERT OR IGNORE INTO meals
											(mealName,Calories,Protien,Carbs,Fats) VALUES 	(?,?,?,?,?)
									""",(name,cal,pro,car,fat)) #inserts variables


def deleteMeal():
	pass


deleteTable()
hello()
createTable()
storeMeals("a",1,1,1,1)