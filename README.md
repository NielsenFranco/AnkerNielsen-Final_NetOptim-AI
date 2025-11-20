# NetOptim_AI – Proyecto Final de Investigación Operativa

## Resumen

NetOptim_AI es un prototipo integral para optimizar **ubicación de antenas**, **asignación de espectro** y **simulación de tráfico** en una red 5G.  
El proyecto integra diversas técnicas de Investigación Operativa:

- **P-Median y Location Models**
- **Optimización Convexa (CVXPY)**
- **Teoría de Colas (Erlang B)**
- **Simulación de Eventos Discretos (SimPy)**
- **Teoría de Juegos (Best-Response)**
- **MDP y Value Iteration**
- **Optimización Robusta basada en escenarios (SAA)**

El sistema está completamente integrado para trabajar con **datasets en formato CSV** almacenados en la carpeta `data/`.

---

## ✔ Estructura del repositorio

project_root/
│
├── data/ # datasets reales en CSV
│ ├── nodes.csv
│ ├── clients.csv
│ ├── cell_configs.csv
│ └── spectrum_params.csv
│
├── src/
│ ├── network_graph.py
│ ├── location_models.py
│ ├── spectrum_optimization.py
│ ├── traffic_simulator.py
│ ├── queueing_analysis.py
│ ├── game_theory_solver.py
│ ├── mdp_policies.py
│ ├── robustness_tools.py
│ ├── integrator.py # AHORA carga desde CSV
│ └── main_demo.py # genera outputs CSV + JSON
│
├── dashboard/
│ └── results_dashboard.html
│
├── results/ # salida automática (CSV + JSON)
│
├── requirements.txt
└── README.md

yaml
Copiar código

---

# Instalación

Se recomienda usar `venv`:

```bash
python -m venv venv

Activar entorno virtual
Windows

venv\Scripts\activate

Actualizar pip

python -m pip install --upgrade pip

Instalar dependencias

pip install -r requirements.txt

Dependencias principales (alternativa)

pip install numpy pandas matplotlib networkx simpy cvxpy pulp seaborn

✔ Uso y ejecución
Los datasets deben estar en:


data/nodes.csv
data/clients.csv
data/cell_configs.csv
data/spectrum_params.csv

Ejecutar la demo principal
Desde la raíz del repositorio:


python src/main_demo.py

Esto generará automáticamente:

En results/:
p_median.json

p_median.csv

spectrum.json

spectrum.csv

traffic.json

traffic.csv

Todos estos resultados se basan en los datasets reales en data/.

✔ Dashboard visual
Para visualizar resultados con un entorno gráfico (HTML):

Paso 1 — levantar servidor local
bash
Copiar código
python -m http.server 8000
Paso 2 — abrir en el navegador
Ir a:

bash
Copiar código
http://localhost:8000/dashboard/results_dashboard.html
El dashboard muestra:

Clusters y decisiones del modelo P-Median

Gráfico de asignación de espectro

Gráfico de probabilidades de bloqueo

✔ Descripción de módulos importantes
Archivo	Función
network_graph.py	Construcción del grafo físico de nodos
location_models.py	Implementación P-Median usando ILP (PuLP)
spectrum_optimization.py	Asignación convexa de banda con CVXPY
traffic_simulator.py	Simulación de tráfico con SimPy
queueing_analysis.py	Fórmula Erlang B
game_theory_solver.py	Juego no cooperativo (Best-Response Dynamics)
mdp_policies.py	Value Iteration para políticas de handover
robustness_tools.py	Optimización robusta por escenarios (SAA)
integrator.py	Carga datasets CSV y ejecuta modelos
main_demo.py	Ejecuta pipeline completo y genera métricas