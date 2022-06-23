import numpy as np
from scipy import stats, special
from icecream import ic
n = 20
k = 20

ic (
    # 0. Permutation (Alle und ohne wiederholung)
    special.factorial(n, exact=True),

    # 1. Variation (Geordnete Auswahl)

    # 1.1 ohne Wiederholungen
    special.perm(n, k, exact=True),
    # 1.2 mit Wiederholungen
        # .zB. PIN 4 stellig aus Ziffern 0-9
    pow(n, k),

    # Kombination (Ungeordnete Auswahl)

    # 1.1 ohne Wiederholungen,
        # zB. 2 Socken aus Schublade von 8 Socken ziehen
        # hier dran denken: Häufig in Aufgaben Gegenereignis hilft!
    special.comb(n, k, repetition=False, exact=True),
    # 1.2 mit Wiederholungen,
    special.comb(n, k, repetition=True, exact=True)
)
