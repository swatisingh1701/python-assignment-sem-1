# Name: Swati Singh
# Date: 05 Nov 2025
# Project: Daily Calorie Tracker CLI
 
#Task 1 — Welcome

print("Welcome to Daily Calorie Tracker!")
print("Track your meals, calories, stay within your daily goal, stay healthy.\n")


#Task 2 — Input & Data Collection


meals = []
calories = []

n = int(input("How many meals did you have today?"))

for i in range(n):
    meal_name = input(f"Enter meal name: ")
    calorie = float(input(f"Enter calories for: "))
    meals.append(meal_name)
    calories.append(calorie)


#Task 3 — Calorie Calculations


total_calories = sum(calories)
average_calories = total_calories / len(calories)
daily_limit = float(input("\nEnter your daily calorie limit: "))


#Task 4 — Limit Check


if total_calories > daily_limit:
    print("\n You have exceeded your daily calorie limit!")
else:
    print("\n Great! You are within your daily calorie goal.")



#Task 5 — Neatly Formatted Output


print("\nMeal Name\tCalories")
print("-" * 30)

for i in range(len(meals)):
    print(f"{meals[i]}\t\t{calories[i]}")

print("-" * 30)
print(f"Total:\t{total_calories}")
print(f"Average:\t{average_calories:.2f}")

