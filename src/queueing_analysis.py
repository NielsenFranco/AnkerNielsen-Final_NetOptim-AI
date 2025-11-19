# queueing_analysis.py
# Funciones utiles para analisis de colas M/M/c/k (Erlang B basico)

import math

def erlang_b(traffic, servers):
    """Erlang B formula (probabilidad de bloqueo para trafico dado y servers)"""
    # traffic = lambda / mu (oferta en Erlangs)
    inv_b = 0.0
    for k in range(0, servers+1):
        inv_b += (traffic**k) / math.factorial(k)
    b = ((traffic**servers) / math.factorial(servers)) / inv_b
    return b

if __name__ == "__main__":
    A = 10.0  # Erlangs
    c = 5
    print("Erlang B:", erlang_b(A, c))
