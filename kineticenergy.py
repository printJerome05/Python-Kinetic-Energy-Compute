
import math

mass = int(input("Enter Mass in kilograms: "))
velo = float(input("Enter velocity in meters per second:" ))



velo = velo ** 2

t1 = mass * velo

t2 = 2




                 

def kineticenergy(t1, t2):
    f = t1 / t2
    rd = round ( f, 2)
   
    print("The object's kinetic energy is: ", rd , "J")

kineticenergy(t1, t2 )




