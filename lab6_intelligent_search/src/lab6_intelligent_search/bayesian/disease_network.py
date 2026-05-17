from pgmpy.models import DiscreteBayesianNetwork  # <-- Cambiado aquí
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Cambiado aquí también:
model = DiscreteBayesianNetwork([
    ('Disease', 'Fever'),
    ('Disease', 'Test')
])

cpd_disease = TabularCPD(
    variable='Disease',
    variable_card=2,
    values=[[0.1], [0.9]]
)

cpd_fever = TabularCPD(
    variable='Fever',
    variable_card=2,
    values=[[0.8, 0.2], [0.2, 0.8]],
    evidence=['Disease'],
    evidence_card=[2]
)

cpd_test = TabularCPD(
    variable='Test',
    variable_card=2,
    values=[[0.9, 0.1], [0.1, 0.9]],
    evidence=['Disease'],
    evidence_card=[2]
)

model.add_cpds(cpd_disease, cpd_fever, cpd_test)

inference = VariableElimination(model)