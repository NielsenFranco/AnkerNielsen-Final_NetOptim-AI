# robustness_tools.py
# Generador simple de escenarios y optimizacion por escenarios (sample average)

import random
import numpy as np

def generate_demand_scenarios(base_demand, n_scenarios=50, volatility=0.2, seed=0):
    random.seed(seed)
    scenarios = []
    for _ in range(n_scenarios):
        factor = random.uniform(1-volatility, 1+volatility)
        scenarios.append(base_demand * factor)
    return np.array(scenarios)

def optimize_by_scenarios(solve_func, scenarios):
    """
    solve_func: funcion que recibe un valor de demanda y devuelve costo para una decision
    Esta funcion evalua decisiones discretas y elige la que minimiza porcentaje promedio
    """
    decisions = list(range(0, 201, 10))
    best = None
    best_cost = float('inf')
    for d in decisions:
        costs = [solve_func(scenario, d) for scenario in scenarios]
        avg = sum(costs)/len(costs)
        if avg < best_cost:
            best_cost = avg
            best = d
    return best, best_cost
