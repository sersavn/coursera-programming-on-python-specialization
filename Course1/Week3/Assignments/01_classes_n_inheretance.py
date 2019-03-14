import csv
import os

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        filename = os.path.splitext(str(self.photo_file_name))
        return filename[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        try:
            next(reader)  # пропускаем заголовок
        except: # there is no header, file is empty
            pass
        for row in reader:
            try:
                if row[0] == 'car':
                    the_car = Car(row[1], row[3], float(row[5]), int(row[2]))
                    the_car.car_type = row[0]
                    car_list.append(the_car)
                elif row[0] == 'truck':
                    the_car = Truck(row[1], row[3], float(row[5]), row[4])
                    the_car.car_type = row[0]
                    dim = row[4].split('x')
                    try:
                        the_car.body_width = float(dim[0])
                        the_car.body_height = float(dim[1])
                        the_car.body_length = float(dim[2])
                    except: #if body unknown replace with 0
                        the_car.body_width = 0
                        the_car.body_height = 0
                        the_car.body_length = 0
                    del the_car.body_whl
                    car_list.append(the_car)
                elif row[0] == 'spec_machine':
                    the_car = SpecMachine(row[1], row[3], float(row[5]), row[6])
                    the_car.car_type = row[0]
                    car_list.append(the_car)
            except: # if row[0] is empty
                pass
    return car_list
'''
print(get_car_list("01_coursera_week3_cars.csv"))
print(get_car_list("01_coursera_week3_cars.csv")[0].__dict__)
print(get_car_list("01_coursera_week3_cars.csv")[1].__dict__)
print(get_car_list("01_coursera_week3_cars.csv")[2].__dict__)
print(get_car_list("01_coursera_week3_cars.csv")[3].__dict__)
'''
