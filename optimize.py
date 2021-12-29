import csv
import sys


if __name__ == '__main__':
    def parse_data(data):
        to_compute = []
        meet_name = []
        for d in data:
            if(d['name'] in meet_name):
                old_name = d['name']
                d['name'] = d['name'] + f"-{meet_name.count(d['name'])}"
                meet_name.append(old_name)
            else:
                meet_name.append(d['name'])

            if float(d['price']) > float(0.00):
                if float(d['profit']) > float(0.00):
                    to_compute.append(d)
    
        return to_compute
    filename = ""
    if sys.argv[1] == "data_1":
        filename = 'dataset1_Python+P7.csv'
    if sys.argv[1] == "data_2":
        filename = 'dataset2_Python+P7.csv'

    with open(filename, newline="") as data_file:
        DATA = [dict(data) for data in csv.DictReader(data_file)]
        to_compute = parse_data(DATA)

        sorts_data = lambda x: (-float(x['profit']), float(x['price']))
        sorted_data = sorted(to_compute, key=sorts_data)

        max_price = 500
        index = 0
        bill = 0

        wallet = []
        while index < len(sorted_data) - 1:
            d = sorted_data[index]
            if bill + float(d['price']) <= max_price:
                wallet.append(d)
                bill += float(d['price'])
            index += 1
    
        total_costs = "%0.2f" %sum([float(d['price']) for d in wallet])
        total_gains = "%0.2f" %sum([float(d['price'])*float(d['profit'])/100 for d in wallet])

        print("\nACTION \t\t\t| COST \t| GAIN\n")
        print("\r\n".join([f"{a['name']}\t\t{a['price']}\t{float(a['price'])*float(a['profit'])/100}" for a in wallet]))
        print(f"\nTotal investisement: {total_costs}€ \t| Total gain: {total_gains}€")