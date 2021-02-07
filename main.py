import csv
import json
from my_package import add_price_range, add_car_class

cars_from_file = []
header = ()
car_info = []

with open('homework_example.csv', 'r') as file:
    new_data = csv.reader(file)

    for index, data in enumerate(new_data):
        if index == 0:
            header = data
        else:
            car_info.append(data)
#
cars_from_file = [{key: value for key, value in zip(header, element)} for element in car_info]


# with open('my_output.json', 'w') as json_file:
#     json_file.write(json.dumps(cars_from_file))


cars_from_file = list(map(add_car_class, cars_from_file))
cars_from_file = list(map(add_price_range, cars_from_file))


print(cars_from_file)
