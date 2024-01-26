################
# Lab 2
# Author: Melika Sherafat
# Email: melika.sherafatt@gmail.com
# Student ID: 218970871
# Section B
###############

print("\n----Task 1---- BMI Calculator")
## Write Task1 code here
Name = input("Name: ")
Weight = float(input("Weight(in kg): "))
Weight_2_decimals = "{:.2f}".format(Weight)
Height = float(input("Height(in cm): "))
Height_2_decimals = "{:.2f}".format(Height)
BMI = float(Weight/(Height/100)**2)
Name = Name.lower()
Name = Name.capitalize()
print("Name: ", Name, ", ", "Weight: ", Weight_2_decimals, ", ", "Height: ", Height_2_decimals, ", ", "BMI: ", BMI)





print("\n----Task 2---- Leetspeak Converter")
## Write Task2 code here
leetspeak = input()
leetspeak = leetspeak.upper()
leetspeak = leetspeak.replace(" ", "")
leetspeak = leetspeak.replace("T" , "+")
leetspeak = leetspeak.replace("A" , "@")
leetspeak = leetspeak.replace("E" , "3")
leetspeak = leetspeak.replace("I" , "|")
leetspeak = leetspeak.replace("B" , "8")
leetspeak = leetspeak.replace("S" , "5")
leetspeak = leetspeak.replace("O" , "0")
leetspeak = leetspeak.replace("C" , "[")
print(leetspeak)



print("\n----Task 3---- Flipping String")
## Write Task3 code here
String = input("Long String: ")
String = String.upper()
Middle = String[len(String)//2 - 1]
print("This string is", len(String), " characters long. The middle character is ", "'",Middle,"'")
seperatorindex = String.find(Middle)
letterstring = String[:seperatorindex]
numberstring = String[seperatorindex+1:]
outputstring = (numberstring + "|", letterstring)
print("Flipped string")
print(outputstring)

print("\n----Task 4---- Multiple numbers")
## Write Task4 code here
#I could get this code to extract numbers but could not turn them into int(), and multiply them

String = input("Enter string with two numbers to be multiplied together: ")
numbers = []
for word in String. split():
    if word. isdigit():
        numbers. append(int(word))
print("Extracted numbers:", numbers)

input("Press enter to exit. ")  # input statement to pause code when finished