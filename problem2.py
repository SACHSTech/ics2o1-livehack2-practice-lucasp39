"""
********************************************************
Filename:       problem2.py
Description:    Determine where you get to go on summer vacation
Author:         Pei.L
Created On:     12/02/2021
********************************************************
"""
print("******Summer Vacation Destination Calculator******")

#ask for final grade and earnings
final_grade = float(input("What is your final grade?: "))
earnings = float(input("How much money did you earn?: "))

#calculate and find out destination
if final_grade >= 80 and earnings >= 500:
  print("Congrats! You are going to Europe!")
elif final_grade >= 80 and earnings < 500:
  print("You are going to California!")
else: 
  print("You have to stay at home.")