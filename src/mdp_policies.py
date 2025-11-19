# mdp_policies.py
# Plantilla simple de MDP con value iteration para decision de handover entre 2 celdas
# Estados: (load_bin_cell1, load_bin_cell2) con tres bins 0,1,2
# Acciones: 0 = no action, 1 = handover una sesion de 1->2, 2 = handover 2->1

import itertools
import math

def build_mdp():
    states = [(i,j) for i in range(3) for j in range(3)]
    actions = [0,1,2]
    # transiciones y recompensas simplificadas
    P = {}
    R = {}
    for s in states:
        for a in actions:
            # placeholder: permanecer en el mismo estado con penalizacion segun carga
            P[(s,a)] = [(1.0, s)]
            R[(s,a)] = - (s[0] + s[1])  # penaliza carga total
    return states, actions, P, R

def value_iteration(states, actions, P, R, gamma=0.95, eps=1e-3):
    V = {s: 0.0 for s in states}
    policy = {s: 0 for s in states}
    while True:
        delta = 0
        for s in states:
            vals = []
            for a in actions:
                val = R[(s,a)] + gamma * sum(p * V[s2] for (p,s2) in P[(s,a)])
                vals.append(val)
            best = max(vals)
            V_new = best
            delta = max(delta, abs(V_new - V[s]))
            V[s] = V_new
            policy[s] = actions[vals.index(best)]
        if delta < eps:
            break
    return V, policy

if __name__ == "__main__":
    states, actions, P, R = build_mdp()
    V, policy = value_iteration(states, actions, P, R)
    print("Politica:", policy)
