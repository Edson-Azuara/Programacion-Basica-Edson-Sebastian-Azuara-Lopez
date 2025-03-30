#Problema 33

import csv

with open('personas.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print('ap paterno: {0}, ap materno: {1}, nombres : {2}, cuidad: {3}'.format(row[0], row[1], row[2], row[3]))
