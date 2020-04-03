"""
https://sph.umich.edu/pursuit/2020posts/how-scientists-quantify-outbreaks.html
"""

import csv
from datetime import datetime

datosMX = []
N = 126577691

h = 1


def lector(archivo):
    global datosMX
    with open(archivo, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are: {", ".join(row)}')
            else:
                if row[0] == 'Mexico':
                    datosMX.append(row)
            line_count += 1


def a_nm(In, Im, Sn, Sm):
    global h
    global N
    return (Sn * In - Sm * Im) * h / N


def b_nm(In, Im):
    global h
    return (In - Im) * h


def c_nmpq(a_nm, a_pq, b_nm, b_pq):
    return (b_nm * a_pq / a_nm) - b_pq


def gamma(index):
    global datosMX
    global N

    I3 = float(datosMX[index][2])
    I2 = float(datosMX[index - 1][2])
    I1 = float(datosMX[index - 2][2])
    I0 = float(datosMX[index - 3][2])

    death = datosMX[index - 1][4]
    recover = datosMX[index - 1][3]
    R2 = 0.0
    if len(death) > 0:
        R2 += float(death)
    if len(recover) > 0:
        R2 += float(recover)

    death = datosMX[index - 2][4]
    recover = datosMX[index - 2][3]
    R1 = 0.0
    if len(death) > 0:
        R1 += float(death)
    if len(recover) > 0:
        R1 += float(recover)

    death = datosMX[index - 3][4]
    recover = datosMX[index - 3][3]
    R0 = 0.0
    if len(death) > 0:
        R0 += float(death)
    if len(recover) > 0:
        R0 += float(recover)

    S0 = N - I0 - R0
    S1 = N - I1 - R1
    S2 = N - I2 - R2

    aux = I3 - 2 * I2 + I1

    a10 = a_nm(I1, I0, S1, S0)
    a21 = a_nm(I2, I1, S2, S1)

    b10 = b_nm(I1, I0)
    b21 = b_nm(I2, I1)

    if a10 == 0:
        return -1.0

    c1021 = c_nmpq(a10, a21, b10, b21)

    aux += (-I2 + 2 * I1 - I0) * a21 / a10

    if c1021 == 0:
        return -1.0

    aux /= c1021

    return aux


def beta(index, g):
    global datosMX
    global N

    if g < 0:
        return -1.0

    I2 = float(datosMX[index - 1][2])
    I1 = float(datosMX[index - 2][2])
    I0 = float(datosMX[index - 3][2])

    death = datosMX[index - 2][4]
    recover = datosMX[index - 2][3]
    R1 = 0.0
    if len(death) > 0:
        R1 += float(death)
    if len(recover) > 0:
        R1 += float(recover)

    death = datosMX[index - 3][4]
    recover = datosMX[index - 3][3]
    R0 = 0.0
    if len(death) > 0:
        R0 += float(death)
    if len(recover) > 0:
        R0 += float(recover)

    S0 = N - I0 - R0
    S1 = N - I1 - R1

    aux = I2 - 2 * I1 + I0 + b_nm(I1, I0) * g
    a10 = a_nm(I1, I0, S1, S0)
    if a10 > 0:
        aux /= a10
        return aux
    return -1.0


archivo = '/Users/alfonso/devel/datoscovid-19/web-data/data/cases_time.csv'


def main():
    global archivo
    global datosMX

    lector(archivo)
    # print(datosMX)

    i = 0
    for d in datosMX:
        print(d)

        if i > 3:
            I3 = float(datosMX[i][2])
            I2 = float(datosMX[i - 1][2])
            I1 = float(datosMX[i - 2][2])
            I0 = float(datosMX[i - 3][2])
            if I0 > 0 and I1 > 0 and I2 > 0 and I3 > 0:
                g = gamma(i)
                b = beta(i, g)
                print(i, g, b, b / g)
        i += 1

main()
