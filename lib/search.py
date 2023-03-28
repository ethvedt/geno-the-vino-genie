from ref_tables import *

def attr_search(attribute, value):
    if attribute == "meat":
        table = meat_table
    elif attribute == "veg":
        table = veg_table
    elif attribute == "flavor":
        table = flavor_table
    elif attribute == "starch":
        table = starch_table
    elif attribute == "spice":
        table = spice_table
    elif attribute == "dairy":
        table = dairy_table
    return table[value]

def meal_search(food):
    coefficients = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for attribute, value in dir(food):
        attr_coeff = attr_search(attribute, value)
        coefficients = list(map(lambda a, b: a+b, coefficients, attr_coeff))
    return [wine for _, wine in sorted(zip(coefficients, wine_list), key=lambda x: x[0], reverse=True)]

# class Food:

#     def __init__(self, meat, veg, flavor, starch, spice, dairy):
#         self.meat = meat
#         self.veg = veg
#         self.flavor = flavor
#         self.starch = starch
#         self.spice = spice
#         self.dairy = dairy

#     def __dir__(self):
#         return [('meat', self.meat), ('veg', self.veg), ('flavor', self.flavor), ('starch', self.starch), ('spice', self.spice), ('dairy', self.dairy)]

# food1 = Food(meat="red meat", veg="allium", flavor="rich", starch="potato", spice="black pepper", dairy="cream")
# food2 = Food(meat="fish", veg="nightshade", flavor="bitter", starch="sweet veg", spice="herbs", dairy="soft cheese")

# print(meal_search(food1))
# print(meal_search(food2))