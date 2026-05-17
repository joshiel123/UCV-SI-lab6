from lab6_intelligent_search.bayesian.disease_network import inference

def calculate_probability(evidence: dict, target: str = "Disease"):
    """
    Calcula la probabilidad de una variable dado un conjunto de evidencias.
    Ejemplo de evidence: {"Fever": 1, "Test": 0}
    """
    try:
        # Ejecuta la inferencia por eliminación de variables
        result = inference.query(variables=[target], evidence=evidence)
        
        # Extraemos los valores probabilísticos (0: No Enfermo, 1: Enfermo)
        # result.values devuelve un array con las probabilidades
        probabilities = result.values.tolist()
        
        return {
            "target_variable": target,
            "evidence_provided": evidence,
            "probability_distribution": {
                "False (0)": probabilities[0],
                "True (1)": probabilities[1]
            }
        }
    except Exception as e:
        return {"error": str(e)}