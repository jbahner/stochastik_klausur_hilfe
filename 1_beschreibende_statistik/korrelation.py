import numpy as np
from icecream import ic
from scipy import stats, special
import matplotlib.pyplot as plt

# Streudiagramm zeichnen
a = [8,7,5,10,6,3,9,7]
b = [55,60,40,70,45,40,65,55]
c = [3,10,9,1,5,10,2,3]
ic (
    # Korrelationskoeffizient
    np.corrcoef(a,b),

    # Regressionsfunktion
    stats.linregress(a,b))

fig, ax = plt.subplots()
plt.plot(a, b, 'o')
ax.set_xlabel('A')
ax.set_ylabel('B')
plt.show()

# Lineare Regressionfunktion zeichnen
    #reg = stats.linregress(a, b)
    #plt.plot(a, b, 'o', label='original data')
    #plt.plot(a, reg.intercept + reg.slope * np.asarray(a), 'r', label='fitted line')
    #plt.legend()
    #plt.show()
