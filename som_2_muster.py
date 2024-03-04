from scipy import optimize

# demand function and variable cost
a = 40000
b = 500
c = 10


# gewinnfunktion mit 2 segmenten
def f1(params):
    r1, r2 = params
    # helper function demand to read out the demand for a set price
    def demand(x):
        return a-b*x
    return -((r1-c)*demand(r1) + (r2-c)*(demand(r2)-demand(r1))) # negative value because we need to minimize

initial_guess = [2, 1]
result = optimize.minimize(f1, initial_guess,method="Powell")
if result.success:
    fitted_params = result.x
    print("Optimal prices: {}".format(fitted_params))
    print("Maximized revenue: {}".format(-1*result.fun))
else:
    raise ValueError(result.message)


