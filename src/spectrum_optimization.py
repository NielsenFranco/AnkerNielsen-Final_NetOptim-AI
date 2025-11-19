# spectrum_optimization.py
# Asignacion de banda via problema convexo simple con cvxpy
# Maximizamos suma log(1 + alpha_i * b_i) sujeto a suma b_i <= B_total

import cvxpy as cp
import numpy as np

def allocate_band(alpha, B_total):
    """
    alpha: array-like con factor de eficiencia por celda
    B_total: recurso total (ej MHz)
    devuelve: banda asignada por celda
    """
    n = len(alpha)
    b = cp.Variable(n, nonneg=True)
    # utilidad concava log(1 + alpha*b)
    obj = cp.Maximize(cp.sum(cp.log(1 + cp.multiply(alpha, b))))
    constraints = [cp.sum(b) <= B_total]
    prob = cp.Problem(obj, constraints)
    prob.solve(solver=cp.SCS, verbose=False)
    return np.array([max(0, float(v)) for v in b.value])

# ejemplo
if __name__ == "__main__":
    alpha = [0.5, 0.3, 0.7]
    B = 100.0
    b = allocate_band(alpha, B)
    print("Banda asignada:", b, "Suma:", b.sum())
