import csv, json, os, glob
from my_package import add_price_range, add_car_class, add_id

delete = glob.glob('./output_data/*')
for item in delete:
    os.remove(item)

cars_from_file = []
header = ()
car_info = []

csv.register_dialect('csv_dialect',
                     delimiter=',',
                     skipinitialspace=True,
                     quoting=csv.QUOTE_ALL)

with open('homework_example.csv', 'r') as file:
    new_data = csv.reader(file, dialect='csv_dialect')

    for index, data in enumerate(new_data):
        if index == 0:
            header = data
        else:
            car_info.append(data)
#
cars_from_file = [{key: value for key, value in zip(header, element)} for element in car_info]


cars_from_file = list(map(add_car_class, cars_from_file))
cars_from_file = list(map(add_price_range, cars_from_file))
# cars_from_file = list(map(add_id, cars_from_file))


print(cars_from_file)


slow_cars = filter(lambda car: True if car['class'] == 'slow' else False, cars_from_file)
fast_cars = filter(lambda car: True if car['class'] == 'fast' else False, cars_from_file)
sport_cars = filter(lambda car: True if car['class'] == 'sport' else False, cars_from_file)
cheap_cars = filter(lambda car: True if car['price_range'] == 'cheap' else False, cars_from_file)
medium_cars = filter(lambda car: True if car['price_range'] == 'medium' else False, cars_from_file)
expensive_cars = filter(lambda car: True if car['price_range'] == 'expensive' else False, cars_from_file)


sorted_cars = [slow_cars, fast_cars, sport_cars, cheap_cars, medium_cars, expensive_cars]


for category in sorted_cars:
    with open('./output_data/%s.json' % ([k for k, v in locals().items() if v == category][0]), 'w') as file:
        for cars in sorted_cars:
            json.dump(list(category), file)
