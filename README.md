# UCV-SI-lab6

## Vista general

`UCV-SI-lab6` es un proyecto educativo de laboratorio para Sistemas Inteligentes que integra:

- un motor de búsqueda A* para encontrar rutas en un grafo ponderado
- una red bayesiana simple para cálculo de probabilidades condicionales
- una API REST construida con FastAPI para exponer ambos servicios

Esta solución demuestra conceptos de inteligencia artificial aplicada a navegación y diagnóstico probabilístico.

## Tabla de contenidos

- [Características](#características)
- [Arquitectura](#arquitectura)
- [Instalación](#instalación)
- [Ejecución](#ejecución)
- [API](#api)
  - [Buscar ruta](#buscar-ruta)
  - [Inferencia bayesiana](#inferencia-bayesiana)
- [Pruebas](#pruebas)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Dependencias](#dependencias)
- [Notas](#notas)

## Características

- Búsqueda de ruta óptima usando el algoritmo A* sobre un grafo de ejemplo
- Red bayesiana con variables `Disease`, `Fever` y `Test`
- Servicio REST para consultas de ruta e inferencia
- Validación de entrada mediante modelos Pydantic
- Pruebas unitarias con `pytest`

## Arquitectura

- `FastAPI` expone la API REST
- `networkx` crea el grafo y ejecuta `astar_path`
- `pgmpy` construye la red bayesiana y realiza inferencia por eliminación de variables
- `Pydantic` define los esquemas de petición

## Instalación

### Requisitos

- Python 3.11 o 3.12
- Poetry (recomendado)

### Con Poetry

```bash
cd lab6_intelligent_search
poetry install
```

### Con pip

```bash
python -m pip install networkx matplotlib fastapi uvicorn pydantic pgmpy python-multipart pytest
```

## Ejecución

Inicie la aplicación desde la carpeta `lab6_intelligent_search`:

```bash
cd lab6_intelligent_search
poetry run uvicorn lab6_intelligent_search.api.main:app --reload --host 127.0.0.1 --port 8000
```

Luego abra `http://127.0.0.1:8000/docs` para ver la documentación interactiva de Swagger.

## API

### Buscar ruta

- Endpoint: `POST /find-route`
- Descripción: calcula la ruta más corta entre dos nodos del grafo.

#### Request

```json
{
  "start": "A",
  "goal": "F"
}
```

#### Response

```json
{
  "path": ["A", "C", "F"],
  "cost": 7
}
```

#### Ejemplo curl

```bash
curl -X POST "http://127.0.0.1:8000/find-route" \
  -H "Content-Type: application/json" \
  -d '{"start":"A","goal":"F"}'
```

### Inferencia bayesiana

- Endpoint: `POST /bayesian-inference`
- Descripción: calcula la probabilidad posterior de `Disease` dado un conjunto de evidencias.

#### Request

```json
{
  "evidence": {
    "Fever": 1,
    "Test": 0
  }
}
```

#### Response

```json
{
  "target_variable": "Disease",
  "evidence_provided": {
    "Fever": 1,
    "Test": 0
  },
  "probability_distribution": {
    "False (0)": 0.1,
    "True (1)": 0.9
  }
}
```

#### Ejemplo curl

```bash
curl -X POST "http://127.0.0.1:8000/bayesian-inference" \
  -H "Content-Type: application/json" \
  -d '{"evidence":{"Fever":1,"Test":0}}'
```

## Pruebas

Ejecute las pruebas unitarias desde `lab6_intelligent_search`:

```bash
cd lab6_intelligent_search
poetry run pytest
```

## Estructura del proyecto

- `lab6_intelligent_search/pyproject.toml` - configuración del proyecto y dependencias
- `src/lab6_intelligent_search/api/main.py` - definición de la API y endpoints
- `src/lab6_intelligent_search/graph/graph_builder.py` - construcción del grafo de ejemplo
- `src/lab6_intelligent_search/graph/heuristic.py` - heurística para A*
- `src/lab6_intelligent_search/services/search_service.py` - lógica de búsqueda de rutas
- `src/lab6_intelligent_search/bayesian/disease_network.py` - modelo bayesiano y VariableElimination
- `src/lab6_intelligent_search/services/bayesian_service.py` - adaptador de inferencia para la API
- `src/lab6_intelligent_search/models/route_models.py` - modelos Pydantic para solicitudes
- `tests/test_astar.py` - pruebas del algoritmo A*
- `tests/test_bayesian.py` - pruebas de inferencia bayesiana

## Dependencias principales

- `fastapi` - framework web
- `uvicorn` - servidor ASGI
- `networkx` - grafos y algoritmos de búsqueda
- `pgmpy` - modelos probabilísticos bayesianos
- `pydantic` - validación de datos
- `pytest` - marco de pruebas

## Notas

- El grafo de ejemplo contiene los nodos `A`, `B`, `C`, `D`, `E`, `F` y sus conexiones ponderadas.
- La red bayesiana enseña inferencia simple con dos evidencias observables: `Fever` y `Test`.
- Este repositorio es un prototipo académico y puede ampliarse con datos reales, más nodos o variables adicionales.

## Contacto

Para preguntas o mejoras, revisa el código en `lab6_intelligent_search/src` y ajusta el modelo o los endpoints según tus necesidades.

👨‍💻 Autor
Josias Eliel Alfageme Neyra
Email: jalfagemene@ucvvirtual.edu.pe