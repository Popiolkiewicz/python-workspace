'''
Created on 07.06.2016

@author: Hubert
'''

#Przetwarzanie danych

#Odczyt z pliku
txt = open('someFile.txt').read()
print(txt)

import linecache
logfile = open('someFile.txt', 'a')
# row = linecache.getline()

import csv
with open('file.csv') as csvfile:
    slownik = {}
    reader = csv.DictReader(csvfile)
    for row in reader:
#         print(row)
        if(row["id"] == '6'):
            print(row)
        if(row["ocena"] == '2'):
            print(str(row) + " with grade == 2")
#     print(slownik)
        
#Moduly statystyczne

# import scipy
# 
# scipy.mean([1,2,3])
# scipy.median([1,2,3])
# scipy.mode([1,2,3])