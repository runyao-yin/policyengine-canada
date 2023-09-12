from policyengine_canada.model_api import *


class nu_single_status_credit_eligible(Variable):
    value_type = float
    entity = Person
    label = "Nunavut single status credit eligible"
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    def formula(person, period, parameters):
        single_status = ~person.household("is_married", period)
        no_dependants = person.household("count_dependants", period) == 0
        return (single_status & no_dependants)