# run a monte carlo simulation for one trade a day for 10 years
# 260 days a year

import random

trades = 2600
sims = 100
starting_capital = 10000
percent_to_risk = .01
ending_capital = []

for i in range(sims):

    capital = starting_capital
    for j in range(trades):

        percent_change = random.uniform(-1.0, 1.0)
        # print( percent_change )
        capital = capital - (capital * percent_to_risk * percent_change)
        # print(capital)

        if capital <= 0:
            capital = 0
            break

    ending_capital.append(capital)

for ec in sorted(ending_capital):
    print(ec)
