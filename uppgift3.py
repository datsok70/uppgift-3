höjd = int(input("Skriv din höjd (cm):")) 
if höjd >= 140 and höjd <= 195:
    print("Välkommen in") 
else:
    print("Du får inte åka, du är för kort/lång")

try:
    first_name = input("Skriv ditt namn: ")
    last_name = input("Skriv ditt efternamn: ")
    age = int(input("Ålder: "))

    if age >= 18:
        print("Du är vuxen")
    else:
        print("Du är inte myndig, under 18")

    print("Hej! " + first_name + " " + last_name + "!")
    print("Du är", age, "år gammal!")

except ValueError:
    print("Fel! Du måste skriva åldern som ett heltal.")

try:
    weight = float(input("Skriv hur mycket du väger i kg: "))
    height = float(input("Skriv din längd i meter: "))

    bmi = weight / (height ** 2)

    print("Ditt BMI är:", bmi)

except ValueError:
    print("Fel! Du måste skriva siffror.") 
  
import math 
radie = float(input("Skriv cirkelns radie: ")) 
area = radie * radie * math.pi 
print("Cirkelns area är:", area)

import random 

dice = random.randint(1, 6) 
print("Du fick", dice)  