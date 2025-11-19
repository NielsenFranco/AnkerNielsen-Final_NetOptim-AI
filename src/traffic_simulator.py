# traffic_simulator.py
# Simulador basico de trafico por celda usando simpy
# Mide blocking y throughput

import simpy
import random
import numpy as np

class Cell:
    def __init__(self, env, name, capacity_mbps, arrival_rate, mean_duration):
        self.env = env
        self.name = name
        self.capacity = capacity_mbps  # capacidad maxima en Mbps
        self.arrival_rate = arrival_rate  # llegadas por unidad de tiempo
        self.mean_duration = mean_duration
        self.active = 0.0  # carga actual en Mbps
        self.blocked = 0
        self.total = 0
        self.throughput_hist = []

    def user_process(self):
        while True:
            # espera hasta la siguiente llegada
            yield self.env.timeout(random.expovariate(self.arrival_rate))
            demand = max(0.1, random.expovariate(1.0/self.mean_duration))  # demanda en Mbps por sesion (ej simplificado)
            self.total += 1
            if self.active + demand <= self.capacity:
                # se acepta
                self.active += demand
                # registrar throughput
                self.throughput_hist.append((self.env.now, demand))
                # lanzar proceso de finalizacion
                self.env.process(self.end_session(demand))
            else:
                # se bloquea
                self.blocked += 1

    def end_session(self, demand):
        yield self.env.timeout(random.expovariate(1.0/self.mean_duration))
        self.active = max(0.0, self.active - demand)

def run_traffic_simulation(sim_time=100, cell_configs=None):
    if cell_configs is None:
        cell_configs = [
            {"name":"CellA","capacity_mbps":50,"arrival_rate":0.2,"mean_duration":5},
            {"name":"CellB","capacity_mbps":80,"arrival_rate":0.15,"mean_duration":6},
        ]
    env = simpy.Environment()
    cells = []
    for cfg in cell_configs:
        c = Cell(env, cfg["name"], cfg["capacity_mbps"], cfg["arrival_rate"], cfg["mean_duration"])
        cells.append(c)
        env.process(c.user_process())
    env.run(until=sim_time)
    results = {}
    for c in cells:
        results[c.name] = {"total": c.total, "blocked": c.blocked, "blocking_prob": c.blocked / max(1, c.total)}
    return results

if __name__ == "__main__":
    res = run_traffic_simulation(200)
    print(res)
