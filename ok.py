import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

xls = pd.ExcelFile(r"ex.xlsx") #use r before absolute file path 
sheetX = xls.parse(0)
imie = sheetX['Imie']
nazwisko = sheetX['Nazwisko']
Srednia = sheetX['Srednia']
Pelne = []
print(imie)
i = 0
for x in imie:
    x += nazwisko[i]
    i+=1
plt.bar(imie, Srednia)
plt.show()