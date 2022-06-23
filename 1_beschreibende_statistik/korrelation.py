import numpy as np
from icecream import ic
from scipy import stats, special
import matplotlib.pyplot as plt

a = [9,13,15,18,20]
b = [18,37,61,125,59]
ic (
    # Korrelationskoeffizient
    np.corrcoef(a,b),

    # Regressionsfunktion
    stats.linregress(a,b)
)

# Lineare Regressionfunktion zeichnen
    #reg = stats.linregress(a, b)
    #plt.plot(a, b, 'o', label='original data')
    #plt.plot(a, reg.intercept + reg.slope * np.asarray(a), 'r', label='fitted line')
    #plt.legend()
    #plt.show()

# Streudiagramm zeichnen
a = [10,50,30,70,80,60,90,40,10,20,30,50,60]
b = [4,5,2,6,6,8,7,2,7,3,5,1,3]
ic (
    np.corrcoef(a,b),
)
fig, ax = plt.subplots()
plt.plot(a, b, 'o')
ax.set_xlabel('A')
ax.set_ylabel('B')
plt.show()