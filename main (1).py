import math
#Question 1
TempFahrenheit= 99.5
TempCelsius=(((TempFahrenheit-32)*5)/9)
print(TempCelsius)

#Question 1 Bonus 1
TemprCelsius= 32.5
TemprFahrenheit=((TemprCelsius*9/5)+32)
print(TemprFahrenheit)

#Question 1 Bonus 2
# Answer= -40

#Question 2
CircleArea = 346.5
Radius = round(math.sqrt(CircleArea/math.pi), 1)
print(Radius)

#Question 2 Bonus 1
Radius = 10.5
Circumference = Radius*2*22/7
print(Circumference)

#Question 2 Bonus 2
Radius = 3.5
Area1 = Radius**2*22/7
print(Area1)

Radius = 2.1
Area2 = round((Radius**2*22/7), 2)
print(Area2)
#Question 3
print(Area1 - Area2)
T= 33.8
WS= 8.5
WindChill= 35.7 + 0.6*T - 35.75*WS**0.16+ 0.43*T*WS**0.16

print(WindChill)

#Question 3 Bonus 1
#Cannot find answer


#Question 3 Bonus 2
#Cannot find answer
