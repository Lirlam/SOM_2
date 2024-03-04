
import numpy as np
import scipy.optimize as optimize

# demand function and variable cost
a = 40000
b = 500
c = 10

# gewinnfunktion mit 2 segmenten
def f1(params):
    def demand(x):
        return a-b*x

    result = ((params[0]-c)*demand(params[0]))
    param_0 = params[0]

    for i in range(1, len(params)):
        param_0 = params[i - 1]
        param = params[i]
        result += (param - c) * (demand(param) - demand(param_0))

    return result * -1

initial_guess = np.array([1, 3, 6, 8 ,13])

end_results = []

for i in range(1, len(initial_guess) + 1):
    print(list(initial_guess[:i]))

    bounds = [(0, None)] * len(initial_guess[:i])  # Assuming parameters are non-negative
    result = optimize.minimize(f1, initial_guess[:i], method="Powell", bounds=bounds)
    print(result.fun *-1)

    end_results += [result.fun * (-1) - 50000 * len(initial_guess[:i])]
    print(len(initial_guess[:i]))

print(end_results)



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

