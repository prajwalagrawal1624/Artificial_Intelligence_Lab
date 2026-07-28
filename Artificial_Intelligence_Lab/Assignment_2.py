# write a python program to accept marks of 5 subjects, calculate total percentage and determine wheather student passed with second class, first class or distinction 40% to 65% is second class , 65% to 75% is first class and 75% or more is distination in python 
# Accept marks of 5 subjects
m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))

#Calculate total marks and percentage 
total = m1 + m2 + m3 + m4+ m5
percentage = total/5

#Display total marks percentage
print("Total Marks =", total)
print("Percentage =", percentage, "%")

 # Determine class
if percentage >= 75:
    print("Result: Distinction")
elif percentage >= 65:
    print("Result: First Class")
elif percentage >= 40:
    print("Result: Second Class")
else:
    print("Result: Fail")

