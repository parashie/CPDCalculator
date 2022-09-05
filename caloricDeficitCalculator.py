import math

# this calculator is not meant to replace a dietician, doctor, or nutritionist it is purely for calculation purposes
# This calculator takes the users weight in pounds, goal in pounds, subtracts the two and converts the difference into calories
# calculate the calories needed to lose weight per day



# 1 pound of fat is 3500 calories
pound = 3500 

#ask the user their current weight and goal weight
currentWeight = float(input("Enter your current weight: ")) 
goalWeight = float(input("Enter your goal weight: ")) 

#find the difference between the current weight and the goal weight
totalDifference = (currentWeight - goalWeight) 
# print(totalDifference)

#convert the difference to calories
totalDifferenceCalories = totalDifference * pound 
# print(totalDifferenceCalories)

#ask the user how many days they want to lose the weight in
timeSpan = float(input("Enter the amount of time you want to lose weight in days: ")) 

#calculate the amount of calories to lose per day
caloricDeficitInDay = totalDifferenceCalories / timeSpan 
# print(caloricDeficitInDay)

#ask user how many calories they eat per day
currentCaloriesConsumed = float(input("Enter the amount of calories you consume per day: "))

#calculate the amount of calories to eat per day to lose weight
CPDNeeded = currentCaloriesConsumed - caloricDeficitInDay
# print(CPDNeeded)

print("You need to consume", CPDNeeded, "calories per day to lose weight.")







