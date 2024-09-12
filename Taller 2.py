import pandas as pd
import numpy as np
import xlsxwriter as xl
dataset = pd.read_excel(r'C:\Users\Aprendiz\Desktop\Santiago ADSO-13\Taller python\ventas.xlsx', 
                        engine ='openpyxl', 
                        header = 0)

print(dataset)
#print(type(dataset))
#lis = dataset.to_numpy().tolist()
serie = pd.Series(dataset.to_numpy().tolist())
print(serie)
#print(type(serie))
print(serie[4][5]*serie[4][6])

#para recorrer la serie
temp = 0
for Z in range(len(serie)):
    if serie[Z][0]=='SAOVia_48':
        temp += serie[Z][5]*serie[Z][6]
print(temp)

for Z in range(len(serie)):
    temp += serie[Z][5]*serie[Z][6]
print(temp)

print(len(serie))



#para poder ejecutar la multiplicacion total y suma usar el input tienda
"""tienda = str(input('ingrese tienda: '))
for Z in range(len(serie)):
    if serie[Z][0]== tienda
        temp += serie[Z][5]*serie[Z][6]
print(temp)"""
