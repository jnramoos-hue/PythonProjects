# Object-Oriented Programming: Programming Paradigms
# Classes and Objects

class Vehicle:
    def move(self):
        print(f'I am a vehicle and I move!')

    def __init__(self, manufacturer, model):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__registration_number = None

    # Setter
    def set_registration_number(self, registration):
        self.__registration_number = registration

    # Getter
    def get_manufacturer_model(self):
        print(f'Model: {self.__model}, Manufacturer: {self.__manufacturer}.\n')

    def get_registration_number(self):
        return self.__registration_number


class Car(Vehicle):
    def move(self):
        print(f'I am a car and I drive on the streets!')


class Motorcycle(Vehicle):
    def move(self):
        print(f'I go very fast!')


class Airplane(Vehicle):
    def __init__(self, manufacturer, model, category):
        self.__category = category
        super().__init__(manufacturer, model)

    def get_category(self):
        return self.__category

    def move(self):
        print(f'I fly high!')


if __name__ == '__main__':
    my_vehicle = Vehicle('GM', 'Cadilac Escalade')
    my_vehicle.move()
    my_vehicle.get_manufacturer_model()
    my_vehicle.set_registration_number('490320-1')
    print(f'Registration: {my_vehicle.get_registration_number()}\n')

    my_car = Car('Volkswagen', 'Polo')
    my_car.move()
    my_car.get_manufacturer_model()

    your_car = Car('Audi', 'Sportback')
    your_car.move()
    your_car.get_manufacturer_model()

    motorcycle = Motorcycle('Harley-Davidson', 'Nighter Special')
    motorcycle.move()
    motorcycle.get_manufacturer_model()

    my_airplane = Airplane('Boeing', '747', '747-8')
    my_airplane.move()
    my_airplane.get_category()
    my_airplane.get_manufacturer_model()