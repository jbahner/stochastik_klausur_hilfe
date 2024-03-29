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
if False:
    a = 50
    b = 180

    x = 100
    quantil = 0.1
    ic("GLEICHVERTEILUNG")
    ic(
        f"P(X = {x})",
        stats.uniform(a, b-a).pdf(x),

        f"P(X <= {x})",
        stats.uniform(a, b-a).cdf(x),
        f"P(X > {x})",
        1 - stats.uniform(a, b-a).cdf(x),
        f"P(X < {x})",
        stats.uniform(a, b-a).cdf(x) - stats.uniform(a, b-a).pdf(x),

        f"P-Quantil {quantil}",
        stats.uniform(a, b-a).ppf(quantil),

        "E(X)",
        stats.uniform(a, b-a).expect(),

        "Var(X)",
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
if False:
    l = 7
    x = 2/7
    quantil = 0.9
    ic("EXPONENTIALVERTEILT")
    ic(
        f"P(X = {x})",
        stats.expon(scale=1/l).pdf(x),

        f"P(X <= {x})",
        stats.expon(scale=1/l).cdf(x),
        f"P(X > {x})",
        1 - stats.expon(scale=1/l).cdf(x),
        F"P(X < {x})",
        stats.expon(scale=1/l).cdf(x) - stats.expon(scale=1/l).pdf(x),

        f"P-Quantil {quantil}",
        stats.expon(scale=1/l).ppf(quantil),

        "E(X)",
        stats.expon(scale=1/l).expect(),

        "Var(X)",
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
if False:
    erw = 13
    std = 1
    quantil = 0.965

    x= 11
    ic("NORMALVERTEILT")
    ic(
        f"P(X = {x})",
        stats.norm(erw, std).pdf(x),

        f"P(X <= {x})",
        stats.norm(erw, std).cdf(x),
        f"P(X > {x})",
        1 - stats.norm(erw, std).cdf(x),

        f"P-Quantil {quantil}",
        stats.norm(erw, std).ppf(quantil),

        "E(X)",
        stats.norm(erw, std).expect(),

        "Var(X)",
        stats.norm(erw, std).var(),    
    )

