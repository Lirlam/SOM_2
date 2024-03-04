from scipy import optimize

# demand function and variable cost
a = 40000
b = 500
c = 10


# Gewinnfunktion mit variabler Anzahl von Segmenten
def total_profit(prices):
    num_segments = len(prices) + 1

    # Hilfsfunktion zur Nachfrageberechnung für einen bestimmten Preis
    def demand(x):
        return a - b * x

    # Berechnung des Gesamtgewinns über alle Segmente
    total_rev = 0
    for i in range(num_segments):
        if i == 0:
            total_rev += (prices[i] - c) * demand(prices[i])
        elif i == num_segments - 1:
            total_rev += (prices[i - 1] - c) * (demand(prices[i - 1]) - demand(prices[i]))
        else:
            total_rev += (prices[i] - c) * (demand(prices[i]) - demand(prices[i - 1]))

    return -total_rev


initial_guess = [2, 1]
result = optimize.minimize(total_profit, initial_guess, method="Powell")
if result.success:
    fitted_prices = result.x
    num_segments = len(fitted_prices) + 1
    print("Optimal prices for {} segments: {}".format(num_segments, fitted_prices))
    print("Maximized revenue: {}".format(-1 * result.fun))
else:
    raise ValueError(result.message)
