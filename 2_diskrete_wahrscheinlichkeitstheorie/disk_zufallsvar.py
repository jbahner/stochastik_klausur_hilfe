# Verteilungsdichtefunktion: f(x)
# 
# Verteilungsfunktion: F(X) 
# wie groß ist die Wahrs. dass Zufallsvariable X einen Wert annimmt der kleiner oder gleich x ist
# Achtung:
# hier muss aufsummiert werden, wenn man sie bestimmen soll
#
# Ergeinisraum:
# Alle potentiellen Ergebnisse 
# z.b. O = {(1), (1,2), (1,3), ...}
#
# Wertebereich / Träger
# Alle möglichen Ausprägungen der Zufallsvariable X
# z.b: X = {1,2,3,4,5})

import numpy as np
from icecream import ic
import matplotlib.pyplot as plt

# Interval
X = [0, 1, 1, 1, 2, 2, 2, 3]
T = np.linspace(0,3,4)
T_add = np.linspace(0,4,5) # hier auf beide hinteren Zahlen + 1
p, _, _ = plt.hist(X, T_add, density=True)

# ohne Interval (z.b. Lose 0€ 1€ 99€)
    # X = [25, 30, 45]
    # T = np.linspace(0,45,46)
    # T_add = np.linspace(0,46,47)
    # p, _, _ = plt.hist(X, T_add, density=True)
X = [0.5,]
# von Hand: Script Teil 2
#  suchen "Diskrete Wahrscheinlichkeitstheorie"
# 4.2
# Erwartungswert: jedes P(X) * X
# Varianz: Für Jedes X: (X - E)^2 * P(X)
ic(
    X, # Zufallsvariable
    T, # Interval (diskret)
    np.cumsum(p), # Verteilungsfunktion
    np.sum(T*p), # Erwartungswert
    np.var(X, ddof=0), # Varianz
    np.std(X, ddof=0), # Standardabweichung

    # Wert in Verteilungsfunktion einsetzen
    # np.cumsum(p)[2 - 1]
)

#plt.bar(T, p)
#plt.step(X, np.cumsum(p))
#plt.show()
