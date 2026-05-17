from lab6_intelligent_search.services.bayesian_service import calculate_probability

def test_bayesian_inference_with_fever():
    # Probamos qué pasa si el paciente presenta Fiebre (Fever = 1)
    result = calculate_probability(evidence={"Fever": 1})
    
    assert "probability_distribution" in result
    # La probabilidad de tener la enfermedad debería cambiar con evidencia
    assert result["probability_distribution"]["True (1)"] > 0.0

def test_bayesian_inference_clear():
    # Si no hay evidencia, pasamos un diccionario vacío
    result = calculate_probability(evidence={})
    
    # Según cpd_disease = [[0.1], [0.9]], Disease=0 es 0.1 y Disease=1 es 0.9
    assert abs(result["probability_distribution"]["True (1)"] - 0.9) < 1e-5