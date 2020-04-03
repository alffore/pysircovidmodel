"""
Lector de CSV de datos

https://www.journaldev.com/23365/python-string-to-datetime-strptime

"""
import csv
from datetime import datetime

N = 126577691

datosMX = {}
datosMX2 = []


def lector(archivo):
    global datosMX
    with open(archivo, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1

            if row['Country/Region'] == 'Mexico':
                datosMX = row
            line_count += 1


def lector2(archivo):
    global datosMX2
    with open(archivo, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are: {", ".join(row)}')
            else:
                if row[1] == 'Mexico':
                    datosMX2 = row
            line_count += 1


def a_nm(In, Im, Sn, Sm, h, N):
    return (Sn * In - Sm * Im) * h / N


def b_nm(In, Im, h):
    return (In - Im) * h


def c_nmpq(a_nm, a_pq, b_nm, b_pq):
    return (b_nm * a_pq / a_nm )- b_pq


def gamma(index):
    global datosMX2

    return


def beta(index, g):
    global datosMX2

    return


archivo = '/Users/alfonso/devel/datoscovid-19/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

lector(archivo)
print(datosMX)

lector2(archivo)
print(datosMX2)

i = 0
for k in datosMX:
    print(k, datosMX[k])
    i += 1
    if i > 4:
        datetime_object = datetime.strptime(k, '%m/%d/%y').date()
        print(i-4,k, datetime_object,datosMX[k])
        if i >= 8:
            print(f"i: {i} calcula gamma y beta")
