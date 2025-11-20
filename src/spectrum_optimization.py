# spectrum_optimization.py
# Optimización convexa del espectro ahora leyendo CSV

import cvxpy as cp
import numpy as np
import pandas as pd

def load_spectrum_params():
    df = pd.read_csv("data/spectrum_params.csv")
    row = df.iloc[0]
    alpha = [row["alpha_0"], row["alpha_1"], row["alpha_2"]]
    B = float(row["B_total"])
    return alpha, B

def allocate_band(alpha, B_total):
    n = len(alpha)
    b = cp.Variable(n, nonneg=True)
    obj = cp.Maximize(cp.sum(cp.log(1 + cp.multiply(alpha, b))))
    constraints = [cp.sum(b) <= B_total]
    prob = cp.Problem(obj, constraints)
    prob.solve(solver=cp.SCS, verbose=False)
    return np.array([float(max(0, v)) for v in b.value])
