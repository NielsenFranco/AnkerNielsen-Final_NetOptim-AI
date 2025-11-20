# traffic_simulator.py
# Simulación desde cell_configs.csv

import simpy
import random
import numpy as np
import pandas as pd

class Cell:
    def __init__(self, env, name, capacity_mbps, arrival_rate, mean_duration):
        self.env = env
        self.name = name
        self.capacity = capacity_mbps
        self.arrival_rate = arrival_rate
        self.mean_duration = mean_duration
        self.active = 0.0
        self.blocked = 0
        self.total = 0
        self.throughput_hist = []

    def user_process(self):
        while True:
            yield self.env.timeout(random.expovariate(self.arrival_rate))
            demand = max(0.1, random.expovariate(1.0 / self.mean_duration))
            self.total += 1

            if self.active + demand <= self.capacity:
                self.active += demand
                self.throughput_hist.append((self.env.now, demand))
                self.env.process(self.end_session(demand))
            else:
                self.blocked += 1

    def end_session(self, demand):
        yield self.env.timeout(random.expovariate(1.0 / self.mean_duration))
        self.active = max(0.0, self.active - demand)

def run_traffic_simulation(sim_time=200, cell_configs=None):
    # Cargar CSV si cell_configs no fue pasado
    if cell_configs is None:
        df = pd.read_csv("data/cell_configs.csv")
        cell_configs = df.to_dict(orient="records")

    env = simpy.Environment()
    cells = []

    for cfg in cell_configs:
        c = Cell(env, cfg["name"], cfg["capacity_mbps"], cfg["arrival_rate"], cfg["mean_duration"])
        cells.append(c)
        env.process(c.user_process())

    env.run(until=sim_time)

    results = {}
    for c in cells:
        results[c.name] = {
            "total": c.total,
            "blocked": c.blocked,
            "blocking_prob": c.blocked / max(1, c.total)
        }

    return results
