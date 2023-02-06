from policyengine_canada.model_api import *


class bc_climate_action_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "British Columbia Climate Action Tax Credit after reduction"
    unit = CAD
    documentation = "Universal amount without adjustment based on AFNI"
    definition_period = YEAR

    def formula(household, period, parameters):
        province = household("province", period)
        income = household("adjusted_family_net_income", period)
        married = household("is_married", period)
        single_parent = household(
            "bc_climate_action_tax_credit_single_parent_household", period
        )
        family = married | single_parent
        base = household("bc_climate_action_tax_credit_base", period)
        p = parameters(period).gov.provinces.bc.tax.income.credits.bccatc
        in_bc = province == province.possible_values.BRITISH_COLUMBIA
        post_reduction = max_(
            where(
                family,
                base - p.family_reduction_rate.calc(income),
                base - p.single_reduction_rate.calc(income),
            ),
            0,
        )
        print(post_reduction)
        return in_bc * post_reduction
