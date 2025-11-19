# integrator.py
# Funciones utilitarias para integrar modulos y generar datos sinteticos

from network_graph import build_random_candidates
from location_models import solve_p_median
from spectrum_optimization import allocate_band
from traffic_simulator import run_traffic_simulation
import os
import json

def generate_synthetic_data(n_nodes=16):
    nodes = build_random_candidates(n_nodes, x_max=20, y_max=20, seed=42)
    # generar demanda por cliente (simplificado)
    clients = nodes[:]
    facilities = nodes[:]
    return clients, facilities

def simple_p_median_demo():
    clients, facilities = generate_synthetic_data(16)
    opens, assign = solve_p_median(clients, facilities, p=3)
    return opens, assign

def simple_spectrum_demo():
    alpha = [0.5,0.4,0.8]
    B = 100.0
    b = allocate_band(alpha, B)
    return b

def simple_traffic_demo():
    res = run_traffic_simulation(sim_time=200)
    return res
