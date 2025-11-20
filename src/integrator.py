# integrator.py
# Integración del proyecto: ahora lee datos desde /data/*.csv

import pandas as pd
from location_models import solve_p_median
from spectrum_optimization import allocate_band
from traffic_simulator import run_traffic_simulation

# -------------------------
# Cargar datasets desde CSV
# -------------------------

def load_nodes():
    df = pd.read_csv("data/nodes.csv")
    return list(zip(df["x"], df["y"]))

def load_clients():
    df = pd.read_csv("data/clients.csv")
    return list(zip(df["x"], df["y"]))

def load_cell_configs():
    df = pd.read_csv("data/cell_configs.csv")
    return df.to_dict(orient="records")

def load_spectrum_params():
    df = pd.read_csv("data/spectrum_params.csv")
    row = df.iloc[0]
    alpha = [row["alpha_0"], row["alpha_1"], row["alpha_2"]]
    B = float(row["B_total"])
    return alpha, B


# -------------------------
# Ejecuciones demo
# -------------------------

def p_median_demo(p=3):
    clients = load_clients()
    facilities = load_nodes()
    opens, assign = solve_p_median(clients, facilities, p)
    return opens, assign

def spectrum_demo():
    alpha, B = load_spectrum_params()
    b = allocate_band(alpha, B)
    return b

def traffic_demo():
    cell_configs = load_cell_configs()
    res = run_traffic_simulation(cell_configs=cell_configs)
    return res
