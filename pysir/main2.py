"""
Código principal que calcula un modelo SIR

https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology
https://www.youtube.com/watch?v=Qrp40ck3WpI
https://www.youtube.com/watch?v=NKMHhm2Zbkw
https://www.youtube.com/watch?v=UENds3fKssM
https://www.youtube.com/watch?v=wEvZmBXgxO0

Datos
https://github.com/CSSEGISandData/COVID-19

AAFR, 27 de marzo del 2020

"""
import numpy as np

N = 126577691 * .70
beta = 0.0004649569271847341
gamma = 41196.64926689799

I0 = 1378
R0 = 29
S0 = N - I0 - R0


def sprima(i, s):
    global beta
    return -beta * i * s


def iprima(I, S):
    global beta
    global gamma
    return (beta * I * S) - gamma * I


def rprima(I):
    global beta
    return beta * I


# Entrada a la rutina principal

def main():
    s = S0
    i = I0
    r = R0
    t = 0
    for h in np.arange(0.0, 100.0, 1):
        s = s + sprima(i, s) * h
        i = i + iprima(i, s) * h
        r = r + rprima(i) * h
        t += h
        print(t, ',', s, ',', i, ',', r, ',', N - r)
        if i <= 0:
            return
    return


main()
