from ref_tables import *

def attr_search(attribute, value):
    return dispatch_table[attribute][value]

def meal_search(meal):
    coefficients = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for attribute, value in meal.vals():
        if attribute not in ['id', 'name']:
            attr_coeff = attr_search(attribute, value)
            coefficients = list(map(lambda a, b: a+b, coefficients, attr_coeff))
    return [wine for _, wine in sorted(zip(coefficients, wine_list), key=lambda x: x[0], reverse=True)]