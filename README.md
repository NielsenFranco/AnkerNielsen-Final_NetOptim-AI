# NetOptim_AI - Proyecto Final Investigacion Operativa

Resumen:
NetOptim_AI es un prototipo para optimizar ubicacion de antenas, asignacion de espectro y simulacion de trafico en una red movil. Integra tecnicas de investigacion operativa: p-median, EOQ-like decisions, optimizacion convexa, teoria de colas, teoria de juegos, MDP y simulacion con simpy.

## Estructura del repositorio:

* data/                       # datos sinteticos generados
* src/

  * network_graph.py
  * location_models.py
  * spectrum_optimization.py
  * traffic_simulator.py
  * queueing_analysis.py
  * game_theory_solver.py
  * mdp_policies.py
  * robustness_tools.py
  * integrator.py
  * main_demo.py
* dashboard/                 # entorno visual para ver resultados
* notebooks/
* results/
* requirements.txt
* README.md

## Instalacion (recomendado usar virtualenv o venv):

```
python -m venv venv
```

### Activar el entorno virtual

**Windows:**

```
venv\Scripts\activate
```

### Actualizar pip

```
python.exe -m pip install --upgrade pip
```

### Instalar dependencias

```
pip install -r requirements.txt
```

### Dependencias principales (si quieres instalarlas manualmente):

```
pip install numpy scipy pandas matplotlib networkx simpy cvxpy pulp seaborn
```

---

## Como ejecutar la demo

Desde la raiz del repositorio:

```
python src/main_demo.py
```

Esto genera automaticamente:

* p_median.json
* spectrum.json
* traffic.json

en la carpeta **results/**.

---

# Ejecutar el dashboard visual en el navegador

Para visualizar los resultados en un entorno grafico amigable, se utiliza el archivo:

```
dashboard/results_dashboard.html
```

### Paso 1: Levantar un servidor local (obligatorio)

Dentro de **netoptim_ai**, ejecutar:

```
python -m http.server 8000
```

### Paso 2: Abrir el dashboard en el navegador

Ingresar a:

```
http://localhost:8000/dashboard/results_dashboard.html
```

Con esto podras ver:

* Resultados del modelo P-Median
* Grafico de asignacion de espectro
* Grafico de probabilidad de bloqueo

---

## Archivos importantes:

* **network_graph.py**: construccion del grafo de ubicaciones
* **location_models.py**: p-median y cobertura
* **spectrum_optimization.py**: asignacion convexa de banda
* **traffic_simulator.py**: simulacion de trafico con simpy
* **queueing_analysis.py**: calculo Erlang B
* **game_theory_solver.py**: best-response para dos operadores
* **mdp_policies.py**: value iteration para politicas MDP
* **robustness_tools.py**: generacion de escenarios
* **main_demo.py**: ejecuta todo y genera resultados reproducibles

---

## Entregables sugeridos para la materia:

* codigo fuente (src/)
* dataset sintetico (data/)
* notebook resumen (notebooks/)
* informe final PDF (docs/informe.pdf)
* presentacion (docs/presentation.pdf)

---

## Notas

* Algunos modulos requieren solvers adicionales para cvxpy como ECOS, OSQP o SCS:

```
pip install ecos osqp scs
```

* El dashboard requiere usar un servidor local para visualizar JSON correctamente.
