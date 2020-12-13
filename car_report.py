import json
import requests
import os

os.system("clear")
inventory = requests.get("https://raw.githubusercontent.com/JohnFu11er/dec_13_morning/main/inventory.json").json()["inventory"]


class Cars():
    
    def __init__(self, make, model, year):
        if not year.isdigit():
            raise Exception(f"Year {year} must be a number.")
        
        self._make = make[:1].upper() + make[1:].lower()
        self._model = model[:1].upper() + model[1:].lower()
        self._year = year
        self._age = 2020 - int(self._year)


    def car_data(self):
        print(f"{self._make[:10]:10} | {self._model[:10]:10} | {self._year:4} | {self._age:3}")

def car_report():
    print("   Make        Model      Year   Age")
    print("*"*36)
    for car in inventory:
        car = Cars(car[0], car[1], car[2])
        Cars.car_data(car)
        
car_report()
