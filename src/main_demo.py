# main_demo.py
# Script que ejecuta demostraciones de los modulos y guarda resultados

import os
from integrator import simple_p_median_demo, simple_spectrum_demo, simple_traffic_demo
import json

def ensure_results_dir():
    if not os.path.exists("results"):
        os.makedirs("results")

def run_all():
    ensure_results_dir()
    print("Ejecutando demo p-median...")
    opens, assign = simple_p_median_demo()
    print("Centros abiertos:", opens)
    with open("results/p_median.json", "w") as f:
        json.dump({"opens": opens, "assign": assign}, f)

    print("\nEjecutando demo spectrum allocation...")
    b = simple_spectrum_demo()
    print("Banda asignada:", b.tolist())
    with open("results/spectrum.json", "w") as f:
        json.dump({"band": b.tolist()}, f)

    print("\nEjecutando demo traffic simulation...")
    res = simple_traffic_demo()
    print("Resultados simulacion:", res)
    with open("results/traffic.json", "w") as f:
        json.dump(res, f)

if __name__ == "__main__":
    run_all()
    print("\\nDemo completa. Revisa la carpeta results/")
