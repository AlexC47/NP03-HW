import csv


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

# cars_from_file = [{key: value for key, value in zip(header, element)} for element in car_info]


def add_car_class(car):
    """
    csv is sepparated by commas, without spaces. the function will fail if the header has no space character.
    :param car:
    :return:
    """
    car = car.copy()
    if int(car[' hp']) < 120:
        car['class'] = 'slow'
    elif 120 <= int(car[' hp']) < 180:
        car['class'] = 'fast'
    else:
        car['class'] = 'sport'

    return car


cars_from_file = list(map(add_car_class, cars_from_file))


def add_price_range(car):
    """
    same as above function
    :param car:
    :return:
    """
    car = car.copy()
    if int(car[' price']) < 1000:
        car['price_range'] = 'cheap'
    elif 1000 <= int(car[' price']) < 5000:
        car['price_range'] = 'medium'
    else:
        car['price_range'] = 'expensive'

    return car