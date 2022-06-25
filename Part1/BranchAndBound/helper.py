# --------------------------------
# Helper tool for Branch and Bound
# --------------------------------

from fractions import Fraction

from pyrsistent import v

items = ['A','B','C','D']
weigths = [8, 24, 19, 16]
values = [11, 38, 57, 64]

maxCapacity = 50

utilityCoefficient = []

for i, new_val in enumerate(values):
    utilityCoefficient.append(new_val/weigths[i])

""" 
for x in utilityCoefficient:
    print(Fraction(x)) """

print("Utility coefficients", utilityCoefficient)

zipped_items = zip(utilityCoefficient, items)
items_sorted = sorted(zipped_items, reverse=True)
items_new_list = [element for _, element in items_sorted]

print("Items =>", items_new_list)

zipped_values = zip(utilityCoefficient, values)
values_sorted = sorted(zipped_values, reverse=True)
values_new_list = [element for _, element in values_sorted]

print("Values =>", values_new_list)

zipped_weigths = zip(utilityCoefficient, weigths)
weigths_sorted = sorted(zipped_weigths, reverse=True)
weigths_new_list = [element for _, element in weigths_sorted]
print("Weigths =>", weigths_new_list)
