"""
Código principal que calcula un modelo SIR

https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology
https://www.youtube.com/watch?v=NKMHhm2Zbkw

Datos
https://github.com/CSSEGISandData/COVID-19

AAFR, 27 de marzo del 2020

"""
import numpy as np

N = 126577691
beta = 0.3
gamma = 0.1
S0 = N
I0 = 717
R0 = 1


def sprima(I, S):
    return -beta * I * S / N


def iprima(I, S):
    return (beta * I * S / N) - gamma * I


def rprima(I):
    return gamma * I


# Entrada a la rutina principal

def main():
    s = S0
    i = I0
    r = R0
    t = 0
    for h in np.arange(0.0, 10.0, 0.01):
        s = s + sprima(i, s) * h
        i = i + iprima(i, s) * h
        r = r + rprima(i) * h
        t = t + h
        print(t, ',', s, ',', i, ',', r, ',', N - r)
        if i <= 0:
            return
    return


main()
