# --------------------------------
# Helper tool for Branch and Bound
# --------------------------------

from fractions import Fraction


weigths = [10, 7, 5, 4]
values = [25, 21, 30, 8]

maxCapacity = 20

utilityCoefficient = []

for i, new_val in enumerate(values):
    utilityCoefficient.append(new_val/weigths[i])

""" 
for x in utilityCoefficient:
    print(Fraction(x)) """

print("Utility coefficients", utilityCoefficient)

zipped_values = zip(utilityCoefficient, values)
values_sorted = sorted(zipped_values, reverse=True)
values_new_list = [element for _, element in values_sorted]

print("Values =>", values_new_list)

zipped_weigths = zip(utilityCoefficient, weigths)
weigths_sorted = sorted(zipped_weigths, reverse=True)
weigths_new_list = [element for _, element in weigths_sorted]
print("Weigths =>", weigths_new_list)
