# main_demo.py
# Ejecuta las demos leyendo datasets reales desde /data/*.csv

import os
import json
from integrator import p_median_demo, spectrum_demo, traffic_demo

def ensure_results_dir():
    if not os.path.exists("results"):
        os.makedirs("results")

def run_all():
    ensure_results_dir()

    # ---------------------------
    # 1. P-MEDIAN
    # ---------------------------
    print("Ejecutando p-median...")
    opens, assign = p_median_demo()
    print("Centros abiertos:", opens)

    with open("results/p_median.csv", "w") as f:
        f.write("facility,opened\n")
        for idx in opens:
            f.write(f"{idx},1\n")

    # JSON también
    with open("results/p_median.json", "w") as f:
        json.dump({"opens": opens, "assign": assign}, f)

    # ---------------------------
    # 2. Spectrum Allocation
    # ---------------------------
    print("\nEjecutando spectrum allocation...")
    b = spectrum_demo()
    print("Banda asignada:", b.tolist())

    with open("results/spectrum.csv", "w") as f:
        f.write("cell,band\n")
        for i, val in enumerate(b):
            f.write(f"{i},{val}\n")

    with open("results/spectrum.json", "w") as f:
        json.dump({"band": b.tolist()}, f)

    # ---------------------------
    # 3. Traffic Simulation
    # ---------------------------
    print("\nEjecutando traffic simulation...")
    res = traffic_demo()
    print("Resultados:", res)

    # CSV
    with open("results/traffic.csv", "w") as f:
        f.write("cell,total,blocked,blocking_prob\n")
        for cell, val in res.items():
            f.write(f"{cell},{val['total']},{val['blocked']},{val['blocking_prob']}\n")

    with open("results/traffic.json", "w") as f:
        json.dump(res, f)

    print("\nDemo completa. Revisa la carpeta results/")

if __name__ == "__main__":
    run_all()
