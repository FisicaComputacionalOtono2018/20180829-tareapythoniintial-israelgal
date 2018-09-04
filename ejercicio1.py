import math
#Vx=input('Escribe la componente en x')
#Vy=input('Escribe la componente en y')
#Vz=input('Escribe la componente en z')
#Vx1=input('Escribe la componente en x1')
#Vy1=input('Escribe la componente en y1')
#Vz1=input('Escribe la componente en z1')
Vx=2
Vy=2
Vz=2
Vx1=1
Vy1=1
Vz1=1
VAB=Vx*Vx1+Vy*Vy1+Vz*Vz1
print(VAB)
MA=math.sqrt(Vx*Vx+Vy*Vy+Vz*Vz)
print(MA)
MB=math.sqrt(Vx1*Vx1+Vy1*Vy1+Vz1*Vz1)
print(MB)
MAB=MA*MB
print(MAB)

angulo=math.acos(VAB/MAB)

angulo2=math.degrees(angulo)
print (angulo2)