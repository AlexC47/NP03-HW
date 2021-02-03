import csv

if __name__ == '__main__':
    pass

cars = {}

with open('homework_example.csv', 'r') as file:
    new_data = csv.reader(file)
    header = []
    car_info = []

    for index, data in enumerate(new_data):
        if index == 0:
            header = new_data
        else:
            car_info.append(new_data)

    print('header', header)
    print('car_info', car_info)
