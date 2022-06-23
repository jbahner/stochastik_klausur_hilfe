# Quantile:
# wenn p Natürliche Zahl: interpolation="midpoint"
# wenn p Komma Zahl: interpolation="nearest"

from configparser import Interpolation
import numpy as np
from scipy import stats, special
import matplotlib.pyplot as plt
import math

from icecream import ic
a = [7,4,10,10,9,3,5,6]
a.sort()
# Median (Zentralwert)
# falls Ungerade Zahl   -> x[m+1]
# falls Gerade Zahl     -> 1/2( x[m] + x[m+1] )

# Quantile:
# wenn n * p = Natürliche Zahl: interpolation="midpoint" 
# 1/2 ( x[np] + x[np +1 ] )

# wenn n * p = Komma Zahl: selbst rechnen. n*p, dann hoch runden, dann dieses Element
# x[np]


ic(
    a,

    np.mean(a), #Mittel
    np.median(a), #Median
    stats.mode(a), #Modalwert

    # Quantile
    # n * p = Natürlich
    np.quantile(a, 0.25, interpolation="midpoint"),
    np.quantile(a, 0.5, interpolation="midpoint"),
    np.quantile(a, 0.75, interpolation="midpoint"),

    # Quantile
    # n * p = Kommazahl
    a[math.ceil(0.6 * len(a)) - 1],

    # Vairanz
    np.var(a, ddof=1),

    # Standardabweichung
    np.std(a, ddof=1),

    # Spannweite
    np.max(a) - np.min(a),

    # Interquatilabstand
    np.quantile(a, 0.75, interpolation="nearest") - np.quantile(a, 0.25, interpolation="nearest"),


)

# PLOT
# plt.hist(a, bins=[0, 10, 20, 30, 40, 50])
# plt.title("My histogram")
# plt.show()