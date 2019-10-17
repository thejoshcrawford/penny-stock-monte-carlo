import csv
import os

percent_change_count = {}

# for each symbol file
files = os.listdir('data')
count = 0
for file in files:

    if not file.endswith(".csv"):
        continue

    print(file)
    # if count > 100:
    #     break

    # count += 1 

    # load the symbol file
    with open('data/' + file) as fp:
        reader = csv.reader(fp)

        previous_price = None
        for line in reader:
            if previous_price is None:
                previous_price = float(line[1])
                continue

            if previous_price == 0:
                previous_price = float(line[1])
                continue

            current_price = float(line[1])
            # print(f'{current_price}')
            # print(f'{previous_price}')
            price_change = (current_price - previous_price)/previous_price
            price_change = round(price_change, 3)
            # print(f'{price_change}')
            percent_change_count[price_change] = percent_change_count.get(price_change, 0) + 1
            previous_price = current_price


# sorted_percents = sorted(percent_change_count)
# print(percent_change_count)
for percent in sorted(percent_change_count.keys()):
    print(f'percent: {percent} count: {percent_change_count[percent]}')


# save the bins


     