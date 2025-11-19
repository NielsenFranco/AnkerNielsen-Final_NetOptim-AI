# game_theory_solver.py
# Best response dynamics para competencia por banda entre dos operadores

import numpy as np

def utility(s, alpha=1.0):
    # utilidad simple: log(1+s) - cost* s
    cost = 0.01
    return np.log(1 + alpha * s) - cost * s

def best_response(other_s, B_total, alpha=1.0):
    # discretizar y buscar mejor s dado other_s
    best = 0
    best_u = -1e9
    for s in np.linspace(0, B_total, 101):
        if s + other_s <= B_total:
            u = utility(s, alpha)
            if u > best_u:
                best_u = u
                best = s
    return best

def find_nash_bilateral(B_total=100):
    s1 = B_total/2
    s2 = B_total/2
    for it in range(100):
        s1 = best_response(s2, B_total)
        s2 = best_response(s1, B_total)
    return s1, s2

if __name__ == "__main__":
    print("Nash approx:", find_nash_bilateral(100))
