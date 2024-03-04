
import numpy as np
import scipy.optimize as optimize

# demand function and variable cost
a= 40000
b= 500
c= 10

# gewinnfunktion mit 2 segmenten
def f1(params):
    def demand(x):
        return a-b*x

    result = ((params[0]-c)*demand(params[0])
    for i in range(2, len(params)):
        result += (params[i]-c)*(demand(params[i])-demand(params[i-1]))
    return results


print(f1([100, 200, 300, 400])

#result = optimize.minimize(f1, initial_guess,method="Powell")



""""
if result.success:
    fitted_params = result.x
    print("Optimal prices: {}".format(fitted_params))
    print("Maximized revenue: {}".format(-1*result.fun))
else:
    raise ValueError(result.message)
"""