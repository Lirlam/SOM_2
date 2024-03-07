#Author: Liam Decaster
#Date: 04.03.2024

import pandas
import numpy as np
import scipy.optimize as optimize

# demand function and variable cost
a = 40000
b = 500
c = 10

# Gewinnfunktion mit n Segmenten
def f1(params):
    # x = Preis, return = Nachfrage (demand)
    def demand(x):
        return a-b*x

    result = ((params[0]-c)*demand(params[0]))
    param_0 = params[0]

    for i in range(1, len(params)):
        param_0 = params[i - 1]
        param = params[i]
        result += (param - c) * (demand(param) - demand(param_0))

    return result * -1


initial_guess = np.array([0, 0, 1, 3, 6])
end_results = []

# Optimierung für n Segmente, wobei n = Anzahl Elemente in initial_guess
for i in range(1, len(initial_guess) + 1):
    bounds = [(0, None)] * len(initial_guess[:i])  # Assuming parameters are non-negative
    result = optimize.minimize(f1, initial_guess[:i], method="Powell", bounds=bounds)
    end_results += [result.fun * (-1) - 50000 * len(initial_guess[:i])]

end_results_rounded = np.round(end_results, 2)

# Ausgabe der Ergebnisse
print("Gewinne:", end_results_rounded, "\n")

print("Max Gewinn: ", max(end_results_rounded),
      "bei ", len(initial_guess[:end_results.index(max(end_results)) + 1]), "Segmenten")


# bounds = [(0, None)] * len(initial_guess)  # Assuming parameters are non-negative
# result = optimize.minimize(f1, initial_guess, method="Powell", bounds=bounds)
# print(result)
#
# if result.success:
#     fitted_params = result.x
#     print("Optimal prices: {}".format(fitted_params))
#     print("Maximized revenue: {}".format(-1*result.fun))
# else:
#     raise ValueError(result.message)



# print("Optimal prices: {}".format(fitted_params


## LIAM

