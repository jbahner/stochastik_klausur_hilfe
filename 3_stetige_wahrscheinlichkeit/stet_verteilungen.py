from scipy import stats
from icecream import ic

# 1 ----- Gleichverteilung -----------
# --------------------------------------
#
#           Bus fährt pünktlich alle 10 Minuten
#
#
#           [a; b]
#           X ~ U(a,b)
a = 2
b = 10

x = 0
ic("GLEICHVERTEILUNG")
ic(
    # P(X = x)      --> Wahrscheinlichkeit, für genau X
    stats.uniform(a, b-a).pdf(x),

    # P(X <= x)     --> Wahrscheinlichkeit, für mindestens/höchstens X
    stats.uniform(a, b-a).cdf(x),
    1 - stats.uniform(a, b-a).cdf(x),

    # P-Quantil
    stats.uniform(a, b-a).ppf(0.1),

    # Erwartungswert
    stats.uniform(a, b-a).expect(),

    # Varianz
    stats.uniform(a, b-a).var(),    
)

# 2 ----- Exponentialverteilung -----------
# --------------------------------------
#
#           Zeit zwischen zwei Ereignissen
#
#           λ = Rate = Erwartungswert = Varianz = 1 / Mittlere Zeit
#           mittlere Zeit zwischen Ereignissen = 1 / λ
#
#           Schuh geht alle 18 Monate kaputt
#           λ = 1/18 
#           
#           
#           X ~ exp(λ)
l = 1/7
x = 2
ic("EXPONENTIALVERTEILT")
ic(
    # P(X = x)      --> Wahrscheinlichkeit, für genau X
    stats.expon(scale=1/l).pdf(x),

    # P(X <= x)     --> Wahrscheinlichkeit, für mindestens/höchstens X
    stats.expon(scale=1/l).cdf(x),
    1 - stats.expon(scale=1/l).cdf(x),

    # P-Quantil
    stats.expon(scale=1/l).ppf(0.1),

    # Erwartungswert
    stats.expon(scale=1/l).expect(),

    # Varianz
    stats.expon(scale=1/l).var(),    
)

# 3 ----- Normalverteilung -----------
# --------------------------------------
#           Standardnormal: Z ~ N(0, 1)
# 
#           Gaußsche Glockenkurve
#
#           µ = Erwartungswert
#           σ = Standardabweichung
#           X ~ N(µ, σ)
erw = 130
std = 15

x= 120
ic("NORMALVERTEILT")
ic(
    # P(X = x)      --> Wahrscheinlichkeit, für genau X
    stats.norm(erw, std).pdf(x),

    # P(X <= x)     --> Wahrscheinlichkeit, für mindestens/höchstens X
    stats.norm(erw, std).cdf(x),
    1 - stats.norm(erw, std).cdf(x),

    # P-Quantil
    stats.norm(erw, std).ppf(0.1),

    # Erwartungswert
    stats.norm(erw, std).expect(),

    # Varianz
    stats.norm(erw, std).var(),    
)

