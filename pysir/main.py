"""
Código principal que calcula un modelo SIR

https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology
https://www.youtube.com/watch?v=Qrp40ck3WpI
https://www.youtube.com/watch?v=NKMHhm2Zbkw
https://www.youtube.com/watch?v=UENds3fKssM

Datos
https://github.com/CSSEGISandData/COVID-19

AAFR, 27 de marzo del 2020

"""
import numpy as np

N = 126577691
beta = 0.00022435893069850434
gamma = 1/15

I0 = 1215
R0 = 28
S0 = N-I0-R0


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
    for h in np.arange(0.0, 100.0, 0.05):
        s = s + sprima(i, s) * h
        i = i + iprima(i, s) * h
        r = r + rprima(i) * h
        t += h
        print(t, ',', s, ',', i, ',', r, ',', N - r)
        if i <= 0:
            return
    return


main()
