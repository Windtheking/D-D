import pandas as pd
import numpy as np
import xlsxwriter as xl
dataset = pd.read_excel(r'D:\Taller python\Ventas_Olimpica_2023.xlsx', 
                        engine ='openpyxl', 
                        header = 0, usecols = "F,G")

print(dataset)
print(type(dataset))