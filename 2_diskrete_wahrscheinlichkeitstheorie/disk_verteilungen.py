from scipy import stats
from icecream import ic
# 1 ----- Bernoulli Verteilung ---------
# --------------------------------------
#
#           Wurf einer Münze
#           Verschicken von 50 Datenpaketen
#   
#           p = Wahrscheinlichkeit, dass etwas eintritt
#           X ~ Ber(p) 




# 2 ----- Gemoetrische Verteilung ------
# --------------------------------------
#
#           Anzahl der Versuche bis zum 1. Erfolg
#           Lebensdauer eines Bauteils
#   
#           p = Wahrscheinlichkeit, dass etwas eintritt
#           X ~ geom(p)
p_2 = 0.55
x_2 = 3
ic ("GEOMETRISCH")
ic (
    # P(X = x)      --> Wahrscheinlichkeit, für genau X
    stats.geom(p_2).pmf(x_2),

    # P(X <= x)     --> Wahrscheinlichkeit, für mindestens/höchstens X
    stats.geom(p_2).cdf(x_2),
    1 - stats.geom(p_2).cdf(x_2),

    # Erwartungswert
    stats.geom(p_2).expect(),

    # Varianz
    stats.geom(p_2).var(),
)


# 3 ----- Binomialverteilung -----------
# --------------------------------------
#
#           Anzahl an erfolgreichen Versuchen 
#           Anzahl an kaputten Bauteilen / Würfe mit Augenzahl 1
#           
#           n = Anzahl an Versuchen
#           p = Wahrscheinlichkeit, dass Erfolg
#           X ~ Bin(n, p)
n_3 = 3
p_3 = 0.55

x_3 = [0]
ic ("BINOMIAL")
ic(
    # P(X = x)      --> Wahrscheinlichkeit, für genau X
    stats.binom(n_3, p_3).pmf(x_3),

    # P(X <= x)     --> Wahrscheinlichkeit, für mindestens/höchstens X
    stats.binom(n_3, p_3).cdf(x_3),
    1 - stats.binom(n_3, p_3).cdf(x_3),


    # Erwartungswert bei Stichprobe
    n_3 * p_3,
    # Erwartungswert
    stats.binom(n_3, p_3).expect(),

    # Varianz
    stats.binom(n_3, p_3).var(),
)

# 4 ----- Hypergeometrische Verteilung -
# --------------------------------------
#
#           Anzahl an Elementen mit best. Eigenschaft aus Stichprobe
#           Ziehen ohne Zurücklegen
#
#           N_g = Grundgesamtheit
#           M = Anzahl an Elementen mit Eigenschaft aus Gesamtheit
#           n = Anzahl Stichprobe
#           X ~ (m, M, N)
N_g_4 = 60
M_4 = 10
n_4 = 3

x_4 = 0
ic("HYPERGEOMETRISCH")
ic (
    # P(X = x)      --> Wahrscheinlichkeit, für genau X
    stats.hypergeom(N_g_4, M_4, n_4).pmf(x_4),

    # P(X <= x)     --> Wahrscheinlichkeit, für mindestens/höchstens X
    stats.hypergeom(N_g_4, M_4, n_4).cdf(x_4),
    1 - stats.hypergeom(N_g_4, M_4, n_4).cdf(x_4),

    # Erwartungswert
    stats.hypergeom(N_g_4, M_4, n_4).expect(),

    # Varianz
    stats.hypergeom(N_g_4, M_4, n_4).var(),
)

# 5 ----- Poisson Verteilung -----------
# --------------------------------------
#
#           Anzahl der Vorkommnisse in einem best. Intervall
#           
#           λ = Auftrittsrate (z.B. 3 pro Woche) 
#           X ~ Po(λ)
#
#           TODO: Wie rechnet man Rate aus wenn Exp() gegeben?
l_5 = 7
x_5 = 5
ic("POISSON")
ic (
    # P(X = x)      --> Wahrscheinlichkeit, für genau X
    stats.poisson(l_5).pmf(x_5),

    # P(X <= x)     --> Wahrscheinlichkeit, für mindestens/höchstens X
    stats.poisson(l_5).cdf(x_5),
    1 - stats.poisson(l_5).cdf(x_5),

    # Erwartungswert
    stats.poisson(l_5).expect(),

    # Varianz
    stats.poisson(l_5).var(),
)