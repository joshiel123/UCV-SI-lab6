from fastapi import FastAPI
from lab6_intelligent_search.models.route_models import RouteRequest, BayesianRequest
from lab6_intelligent_search.services.search_service import find_route
from lab6_intelligent_search.services.bayesian_service import calculate_probability

app = FastAPI(title="Sistema Inteligente de Navegación y Diagnóstico")

@app.post('/find-route')
def search_route(request: RouteRequest):
    return find_route(request.start, request.goal)

# Endpoint adicional para la red bayesiana
@app.post('/bayesian-inference')
def get_inference(request: BayesianRequest):
    return calculate_probability(evidence=request.evidence)