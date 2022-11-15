from policyengine_canada.model_api import *


class family_net_income(Variable):
    value_type = float
    entity = Person
    label = "Family net income"
    unit = CAD
    documentation = "Sum of head and spouse's line 23600 on tax return"
    definition_period = YEAR
