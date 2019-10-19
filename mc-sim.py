# run a monte carlo simulation for one trade a day for 10 years
# 260 days a year

import os
import csv
import random
# import pandas

weighted_changes = {}
weight_sum = 0
with open('out/percent_change_bins.csv') as fp:
        reader = csv.reader(fp)

        for line in reader:
            weighted_changes[float(line[0])] = int(line[1])
            weight_sum += int(line[1])

# print(weight_sum)



# sorted_weights = sorted(weighted_changes.items(), reverse=True)
# print(sorted_weights)
# sorted_weighted_changes = {}
# for elem in sorted_weights :
#     sorted_weighted_changes[elem[0]] = elem[1] 

# print(sorted_weighted_changes)
 
# quit()

trades = 2600
sims = 10
starting_capital = 10000
percent_to_risk = .05
ending_capital = []

for i in range(sims):

    capital = starting_capital
    for j in range(trades):

        random_weight = random.uniform(1, weight_sum)
        for k,v in weighted_changes.items():
            random_weight = random_weight - v 
            if random_weight <= 0:
                percent_change = k
                break 
        # print( percent_change )
        capital = capital - (capital * percent_to_risk * percent_change)
        # print(capital)

        if capital <= 0:
            capital = 0
            break

    ending_capital.append(capital)

# histish = {'>99': 0, '99-95': 0, '95-68': 0, '68-50': 0, '50-34': 0, '34-5': 0, '<1': 0}
sorted_cap = sorted(ending_capital)
# print(sorted_cap)
# for key, val in ending_capital.item():
#     if 95 not in histish and 
#     print(ec)
percentiles = { '99': int(sorted_cap[int(sims * .99)]),
    '95': int(sorted_cap[int(sims * .95)]),
    '68': int(sorted_cap[int(sims * .68)]),
    '50': int(sorted_cap[int(sims * .50)]),
    '34': int(sorted_cap[int(sims * .34)]),
    '5': int(sorted_cap[int(sims * .05)]),
    '1': int(sorted_cap[int(sims * .01)])}

print(percentiles)


# df = pandas.DataFrame(data=ending_capital)
# df.hist()
# df.show()


# print(df.describe())