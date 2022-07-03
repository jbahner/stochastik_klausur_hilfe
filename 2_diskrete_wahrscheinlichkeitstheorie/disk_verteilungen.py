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

if False:
    p = 0.7
    x = 0
    ic("BERNOULLI")
    ic(
        f"P(X = {x})",
        stats.bernoulli(p).pmf(x),

        f"P(X <= {x})",
        stats.bernoulli(p).cdf(x),
        f"P(X > {x})",
        1 - stats.bernoulli(p).cdf(x),

        "E(X)",
        stats.bernoulli(p).expect(),

        "Var(X)",
        stats.bernoulli(p).var(),   
    )


# 2 ----- Gemoetrische Verteilung ------
# --------------------------------------
#
#           Anzahl der Versuche bis zum 1. Erfolg
#           Lebensdauer eines Bauteils
#   
#           p = Wahrscheinlichkeit, dass etwas eintritt
#           X ~ geom(p)
if True:
    p = 0.7
    x = 5
    ic ("GEOMETRISCH")
    ic (
        f"P(X = {x})",
        stats.geom(p).pmf(x),

        f"P(X <= {x})",
        stats.geom(p).cdf(x),
        f"P(X > {x})",
        1 - stats.geom(p).cdf(x),
        f"P(X < {x}",
        stats.geom(p).cdf(x) - stats.geom(p).pmf(x),

        "E(X)",
        stats.geom(p).expect(),

        "Var(X)",
        stats.geom(p).var(),
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
if False:
    n = 3
    p = 0.3

    x = [0]
    ic ("BINOMIAL")
    ic(
        f"P(X = {x})",
        stats.binom(n, p).pmf(x),

        f"P(X <= {x})",
        stats.binom(n, p).cdf(x),
        f"P(X > {x})",
        1 - stats.binom(n, p).cdf(x),
        f"P(X < {x})",
        stats.binom(n, p).cdf(x) - stats.binom(n, p).pmf(x),

        "Erwartungswert bei Stichprobe",
        n * p,
        "E(X)",
        stats.binom(n, p).expect(),

        "Var(X)",
        stats.binom(n, p).var(),
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
if True:
    N_g = 60
    M = 10
    n = 3

    x = 0
    ic("HYPERGEOMETRISCH")
    ic (
        f"P(X = {x})",
        stats.hypergeom(N_g, M, n).pmf(x),

        f"P(X <= {x})",
        stats.hypergeom(N_g, M, n).cdf(x),
        f"P(X > {x})",
        1 - stats.hypergeom(N_g, M, n).cdf(x),

        "E(X)",
        stats.hypergeom(N_g, M, n).expect(),

        "Var(X)",
        stats.hypergeom(N_g, M, n).var(),
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
if False:
    l = 1
    x = 0
    ic("POISSON")
    ic (
        f"P(X = {x})",
        stats.poisson(l).pmf(x),

        f"P(X <= {x})",
        stats.poisson(l).cdf(x),
        f"P(X > {x})",
        1 - stats.poisson(l).cdf(x),

        "E(X)",
        stats.poisson(l).expect(),

        "Var(X)",
        stats.poisson(l).var(),
    )