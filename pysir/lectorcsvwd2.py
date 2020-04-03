import csv
from datetime import datetime

datosMX = []
N = 126577691*0.7

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


def a_param(i2, i1, i0, s0, s1):
    aux = (i1 - i0) / i0
    aux -= (i2 - i1) / i1
    aux /= (s0 - s1)
    return aux


def r_param(i2, i1, i0, s0, s1):
    aux = (i1 - i0) / (i0 * s0)
    aux -= (i2 - i1) / (i1 * s1)
    aux *= s1 * s0
    aux /= (s0 - s1)
    return aux


archivo = '/Users/alfonso/devel/datoscovid-19/web-data/data/cases_time.csv'


def main():
    global archivo
    global datosMX
    global N

    lector(archivo)

    i = 0
    for d in datosMX:
        # print(d)

        if i > 2:
            i2 = float(datosMX[i][2])
            i1 = float(datosMX[i - 1][2])
            i0 = float(datosMX[i - 2][2])

            death = datosMX[i - 2][4]
            recover = datosMX[i - 2][3]
            r0 = 0.0
            if len(death) > 0:
                r0 += float(death)
            if len(recover) > 0:
                r0 += float(recover)

            death = datosMX[i - 1][4]
            recover = datosMX[i - 1][3]
            r1 = 0.0
            if len(death) > 0:
                r1 += float(death)
            if len(recover) > 0:
                r1 += float(recover)

            s0 = N - i0 - r0
            s1 = N - i1 - r1

            if i2 > 0 and i1 > 0 and i0 > 0 and s0 - s1 != 0:
                print(i0, i1, i2, r0, r1, s0, s1)
                a = a_param(i2, i1, i0, s0, s1)
                r = r_param(i2, i1, i0, s0, s1)
                print(f'i:{i} a:{a} r:{r}  aN/r:{a * N / r} r/a:{r/a}')
        i += 1


main()