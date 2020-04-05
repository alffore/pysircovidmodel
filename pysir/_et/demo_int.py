# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html
# https://pundit.pratt.duke.edu/wiki/Python:Ordinary_Differential_Equations

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def x(t):
    return np.cos(3 * t)


def f(t, y, c):
    dydt = x(t) - y / 4
    return dydt


tspan = np.linspace(0, 15, 1000)
yinit = [-1]
c = []

sol = solve_ivp(lambda t, y: f(t, y, c), [tspan[0], tspan[-1]], yinit, t_eval=tspan)

plt.figure(1)
plt.clf()
fig, ax = plt.subplots(num=1)
ax.plot(sol.t, x(sol.t), 'k-', label='Input')
ax.plot(sol.t, sol.y[0], 'k--', label='Output')
ax.legend(loc='best')
plt.show()
