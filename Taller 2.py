dataset = pd.read_excel(r'C:\Users\Aprendiz\Desktop\Santiago ADSO-13\Taller python\ventas.xlsx', 
                        engine ='openpyxl', 
                        header = 0, usecols = "F,G")

print(dataset)
#print(type(dataset))
#lis = dataset.to_numpy().tolist()
serie = pd.Series(dataset.to_numpy().tolist())
print(serie)
#print(type(serie))
