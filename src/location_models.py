# location_models.py
# Implementacion basica del problema p-median usando pulp (ILP)
# Nota: para instancias grandes usar heuristicas

import pulp
import math

def compute_distances(clients, facilities):
    dist = {}
    for i, c in enumerate(clients):
        for j, f in enumerate(facilities):
            d = math.hypot(c[0]-f[0], c[1]-f[1])
            dist[(i,j)] = d
    return dist

def solve_p_median(clients, facilities, p):
    """
    clients: lista de coords de demanda
    facilities: lista de coords candidatas
    p: numero de centros a abrir
    Devuelve: indices de facilities abiertas y asignacion client->facility
    """
    I = range(len(clients))
    J = range(len(facilities))
    dist = compute_distances(clients, facilities)

    prob = pulp.LpProblem("p_median", pulp.LpMinimize)
    y = pulp.LpVariable.dicts('y', J, lowBound=0, upBound=1, cat='Binary')
    x = pulp.LpVariable.dicts('x', [(i,j) for i in I for j in J], lowBound=0, upBound=1, cat='Binary')

    # objetivo
    prob += pulp.lpSum(dist[(i,j)] * x[(i,j)] for i in I for j in J)

    # restricciones
    prob += pulp.lpSum(y[j] for j in J) == p
    for i in I:
        prob += pulp.lpSum(x[(i,j)] for j in J) == 1
        for j in J:
            prob += x[(i,j)] <= y[j]

    # resolver
    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    open_facilities = [j for j in J if pulp.value(y[j]) > 0.5]
    assignment = {i: min(J, key=lambda j: dist[(i,j)] if pulp.value(x[(i,j)])>0.5 else float('inf')) for i in I}
    # mejor devolver asignacion real
    assignment = {}
    for i in I:
        for j in J:
            if pulp.value(x[(i,j)]) > 0.5:
                assignment[i] = j

    return open_facilities, assignment

# ejemplo rapido
if __name__ == "__main__":
    clients = [(1,1),(2,2),(8,8),(9,9)]
    facilities = [(0,0),(5,5),(10,10)]
    p = 2
    opens, asig = solve_p_median(clients, facilities, p)
    print("Abiertas:", opens)
    print("Asignaciones:", asig)
