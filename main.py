from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

CALORIE_GOAL_LIMIT = 3000 #kcal
PROTEIN_GOAL = 180 # grams
FAT_GOAL = 80 # grams
CARBS_GOAL = 300 # grams

today = []

@dataclass
class Food:
    name:str
    calories: int
    protein: int
    carbs: int
    fat: int


done = False

while not done:
    print("""
    (1) Add a new food
    (2) Visualize progress
    (3) Quit
    """)
    

    choice = input("Choose an option: ")

    if choice == "1":
        print("Adding a new food!")
        name = input("Name: ")
        calories = int(input("Calories: "))
        protein = int(input("Protein: "))
        carbs = int(input("Carbs: "))
        fat = int(input("Fat: "))
        food = Food(name, calories, protein, carbs, fat)
        today.append(food)
        print("Succesfully added!")
    elif choice == "2":
        calorie_sum = sum(food.calories for food in today)
        protein_sum = sum(food.protein for food in today)
        carbs_sum = sum(food.carbs for food in today)
        fat_sum = sum(food.fat for food in today)

        fig, axis = plt.subplots(2, 2)
        axis[0, 0].pie([protein_sum, carbs_sum, fat_sum], labels=["Proteins", "Carbs", "Fats"], autopct="%1.1f%%")
        axis[0,0].set_title("Macronutrients Distribution")
        axis[0,1].bar([0,1,2], [protein_sum, carbs_sum, fat_sum], width=0.4)
        axis[0,1].bar([0.5, 1.5, 2.5], [PROTEIN_GOAL, CARBS_GOAL, FAT_GOAL], width=0.4)
        axis[0,1].set_title("Macronutrients Progess")
        axis[1,0].pie([calorie_sum, CALORIE_GOAL_LIMIT - calorie_sum], labels=["Calories", "Remaining"], autopct="%1.1f%%")
        axis[1,0].set_title("Calories Goal Progress")
        axis[1,1].plot(list(range(len(today))), np.cumsum([food.calories for food in today]), label="Calories Eaten")
        axis[1,1].plot(list(range(len(today))), [CALORIE_GOAL_LIMIT] * len(today),  label="Calories Goal")
        axis[1,1].legend()
        axis[1,1].set_title("Calories Goal Over Time")

        fig.tight_layout()
        plt.show()


    elif choice == "3":
        done = True
    else:
        print("Invalid Choice")
