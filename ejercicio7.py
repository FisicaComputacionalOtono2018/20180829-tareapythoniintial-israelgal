stringinput = input("Dame las distancias y los tiempos en formato (d1,t1)(d1,t2), usa (0,0) como ultimo par de datos")
print(stringinput)

stringinput = stringinput.replace(')(',')' ').replace('(',' ').replace(',',' ').replace(')',   ''))
print(stringinput)
for i in stringinput:
         print(int(i))   
print(stringinput)