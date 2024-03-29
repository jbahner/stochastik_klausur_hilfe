# Quantile:
# wenn p Natürliche Zahl: interpolation="midpoint"
# wenn p Komma Zahl: interpolation="nearest"

from configparser import Interpolation
import numpy as np
from scipy import stats, special
import matplotlib.pyplot as plt
import math

from icecream import ic
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

a = [3, 2, 10, 7, 0, 3, 5, 0, 6, 1 ]
a.sort()
# Median (Zentralwert)
# falls Ungerade Zahl   -> x[m+1]
# falls Gerade Zahl     -> 1/2( x[m] + x[m+1] )

# Quantile:
# wenn n * p = Natürliche Zahl: interpolation="midpoint" 
# 1/2 ( x[np] + x[np +1 ] )

# wenn n * p = Komma Zahl: selbst rechnen. n*p, dann hoch runden, dann dieses Element
# x[np]

def mode(array):
    counts = {}
    for e in array:
        if e not in counts:
            counts[e] = 1
        else:
            counts[e] = counts[e] + 1
    max_occ = max(counts.values())
    result = {key:value for (key, value) in counts.items() if value == max_occ}
    return result

ic(
    a,
    "Mittel/Erwartungswert",
    np.mean(a),
    "Median",
    np.median(a),
    "Modalwert",
    mode(a),
    "Varianz",
    np.var(a, ddof=1),
    "Standardabweichung",
    np.std(a, ddof=1),
    "Spannweite",
    np.max(a) - np.min(a),
      
)

# Quantil
quantile = [0.25, 0.5, 0.75] # hier Quantile ändern
for p in quantile:
    quantil = len(a) * p
    if quantil.is_integer():
        ic(
            f"{int(p*100)}%-Quantil",
            np.quantile(a, p, interpolation="midpoint"),
        )
    else:
        ic(
            f"{int(p*101)}%-Quantil",
            a[math.ceil(p * len(a)) - 1],
        )

# Interquartilabstand
x = len(a) * 0.75
if x.is_integer():
    ic(
        "Interquartilabstand",
        np.quantile(a, 0.75, interpolation="nearest") - np.quantile(a, 0.25, interpolation="nearest"),
    )
else:
    ic(
        "Interquartilabstand",
        a[math.ceil(0.75 * len(a)) - 1] - a[math.ceil(0.25 * len(a)) - 1],
)
# PLOT
# plt.hist(a, bins=[0, 10, 20, 30, 40, 50])
# plt.title("My histogram")
# plt.show()

# Violinplots / Geigenplos:
# zeigt Nuancen in der Verteilung, die in Box-Plots nicht wahrnehmbar sind
# 
# Boxplot:
# Zeigt die Außreißer deutlicher. 
# 