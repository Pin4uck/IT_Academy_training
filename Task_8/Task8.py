import abc


class Vehicle(abc.ABC):
    def __init__(self, make, model, year, vin, color, engine, engine_type, max_fuel_volume,
                 fuel_consumption, max_speed, weight, payload, warranty_period, autopilot):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__vin = vin
        self.__color = color
        self.__engine = engine
        self.__engine_type = engine_type
        self.__max_fuel_volume = max_fuel_volume
        self.__fuel_consumption = fuel_consumption
        self.__max_speed = max_speed
        self.__weight = weight
        self.__payload = payload
        self.__max_weight = payload + weight
        self.__warranty_period = warranty_period
        self.__autopilot = autopilot
        self.__fuel_quantity = max_fuel_volume

    def get_make(self):
        return self.__make
    def set_make(self, make):
        self.__make = make

    def get_model(self):
        return self.__model
    def set_model(self, model):
        self.__model = model

    def get_year(self):
        return self.__year
    def set_year(self, year):
        if year > 2021:
            print('Это невозможно!')
            return
        self.__year = year

    def get_vin(self):
        return self.__vin
    def set_vin(self, vin):
        self.__vin = vin

    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color

    def get_engine(self):
        return self.__engine
    def set_engine(self, engine):
        self.__engine = engine

    def get_engine_type(self):
        return self.__engine_type
    def set_engine_type(self, engine_type):
        self.__engine_type = engine_type

    def get_max_fuel_volume(self):
        return self.__max_fuel_volume
    def set_max_fuel_volume(self, max_fuel_volume):
        self.__max_fuel_volume = max_fuel_volume

    def get_fuel_consumption(self):
        return self.__fuel_consumption
    def set_fuel_consumption(self, fuel_consumption):
        self.__fuel_consumption = fuel_consumption

    def get_max_speed(self):
        return self.__max_speed
    def set_max_speed(self, max_speed):
        self.__max_speed = max_speed

    def get_weight(self):
        return self.__weight
    def set_weight(self, weight):
        self.__weight = weight

    def get_payload(self):
        return self.__payload
    def set_payload(self, payload):
        self.__payload = payload

    def get_max_weight(self):
        return self.__max_weight
    def set_max_weight(self, max_weight):
        self.__max_weight = max_weight

    def get_warranty_period(self):
        return self.__warranty_period
    def set_warranty_period(self, warranty_period):
        self.__warranty_period = warranty_period

    def get_autopilot(self):
        return self.__autopilot
    def set_autopilot(self, autopilot):
        self.__autopilot = autopilot

    def get_fuel_quantity(self):
        return self.__fuel_quantity
    def set_fuel_quantity(self, fuel_quantity):
        self.__fuel_quantity = fuel_quantity

    make = property(get_make, set_make)
    model = property(get_model, set_model)
    year = property(get_year, set_year)
    vin = property(get_vin, set_vin)
    color = property(get_color, set_color)
    engine = property(get_engine, set_engine)
    engine_type = property(get_engine_type, set_engine_type)
    max_fuel_volume = property(get_max_fuel_volume, set_max_fuel_volume)
    fuel_consumption = property(get_fuel_consumption, set_fuel_consumption)
    max_speed = property(get_max_speed, set_max_speed)
    weight = property(get_weight, set_weight)
    payload = property(get_payload, set_payload)
    max_weight = property(get_max_weight, set_max_weight)
    warranty_period = property(get_warranty_period, set_warranty_period)
    autopilot = property(get_autopilot, set_autopilot)
    fuel_quantity = property(get_fuel_quantity, set_fuel_quantity)

    def test_system(self):
        if self.engine:
            if not self.fuel_quantity:
                print('Нет топлива!')
                return False
            elif self.fuel_quantity < self.max_fuel_volume / 5:
                print('Проверка прошла успешно!')
                print('Осталось меньше 20% топлива, нужна заправка!')
            else:
                print('Проверка прошла успешно!')
                print(f'Количество топлива: {round(self.fuel_quantity / self.max_fuel_volume * 100)} %')
            return True
        else:
            print('Двигателя нет либо он ек работает!')
            return False

    def start_engine(self):
        if self.test_system():
            print('Двигатель запущен!')
            return True
        else:
            print('Невозможно запустить двигатель!')
            return False

    def move(self, distance):
        if self.start_engine():
            start = 0
            part = distance / 5
            if part < 100:
                part_consumption = 100 / part
                consumption = self.fuel_consumption / part_consumption
            elif part == 100:
                consumption = self.fuel_consumption
            else:
                multiplier = part // 100
                remainder = part % 100
                if remainder:
                    remainder = 100 / remainder
                consumption = self.fuel_consumption * multiplier + remainder
            while start < distance:
                driving = input('Нажимайте Энтер для движения! Или введите "stop" если нужно остановиться')
                if driving == 'stop':
                    self.stop()
                    break
                start += part
                self.fuel_quantity -= consumption
                if self.fuel_quantity < self.max_fuel_volume / 5:
                    if self.fuel_quantity <= 0:
                        self.fuel_quantity = 0
                        print('Топливо кончилось, вы не доехали!')
                        break
                    print(f'Внимание осталось {self.fuel_quantity} литров топлива. Пополните топливо!')
                print(f'Вы проехали {start} км!')
                if start >= distance - 0.5:
                    print('Вы на месте!')
                    break

    @abc.abstractmethod
    def stop(self):
        print('Нажимаем на тормоза!')
        print('Вы остановились!')

    def load_fuel(self, amount):
        if self.engine:
            print(f'Сейчас в баке {self.fuel_quantity} литров топлива!')
            free_space = self.max_fuel_volume - self.fuel_quantity
            print('Открываем заливную горловину.')
            if free_space < amount:
                amount = free_space
                self.fuel_quantity += amount
                print(f'В бак влезло только {amount} литров топлива!')
            else:
                print(f'Успешно заправили на {amount} литров!')
                self.fuel_quantity += amount
            print('Закрываем заливную горловину.')
        else:
            print('У вас нет двигателя!')

    def load_cargo(self, amount):
        print(f'Грузоподъемность авто равна: {self.payload}.')
        if self.payload >= amount:
            print('Открываем багажник.')
            self.payload -= amount
            print(f'Загружаем груз {amount} кг.\nОсторожно! Закрываем багажник.')
        else:
            print(f"Нельзя загрузить {amount} кг.\n")

    def unload_cargo(self, amount):
        weight_cargo = self.max_weight - self.weight - self.payload
        if amount <= weight_cargo:
            self.payload += amount
            print(f'Открываем багажник.')
            weight_cargo -= amount
            print(f'Выгружаем груз {amount} кг.\nОсторожно! Закрываем багажник.')
        else:
            print(f'Нет столько груза! Транспорт загружен на: {weight_cargo} кг.')


class LandVehicle(Vehicle):
    def __init__(self, make, model, year, vin, color, engine, engine_type, max_fuel_volume,
                 fuel_consumption, max_speed, weight, payload, warranty_period, autopilot,
                 axles_count, wheels_count):
        Vehicle.__init__(self, make, model, year, vin, color, engine, engine_type, max_fuel_volume,
                         fuel_consumption, max_speed, weight, payload, warranty_period, autopilot)
        self.__axles_count = axles_count
        self.__wheels_count = wheels_count

    def get_axles_count(self):
        return self.__axles_count
    def set_axles_count(self, axles_count):
        self.__axles_count = axles_count

    def get_wheels_count(self):
        return self.__wheels_count
    def set_wheels_count(self, wheels_count):
        self.__wheels_count = wheels_count

    def move(self, distance):
        return Vehicle.move(self, distance)

    axles_count = property(get_axles_count, set_axles_count)
    wheels_count = property(get_wheels_count, set_wheels_count)


class Car(LandVehicle):
    def __init__(self, make: str, model: str, year: int, vin: str, color: str, engine: bool,
                 engine_type: str, max_fuel_volume: int, fuel_consumption: float, max_speed: int,
                 weight: int, payload: float,
                 warranty_period: int, autopilot: bool, axles_count: int, wheels_count: int,
                 door_count: int, body_type: str, options: list, gears_count: int):
        LandVehicle.__init__(self, make, model, year, vin, color, engine, engine_type, max_fuel_volume,
                             fuel_consumption, max_speed, weight, payload, warranty_period,
                             autopilot, axles_count, wheels_count)
        self.__door_count = door_count
        self.__body_type = body_type
        self.__options = options
        self.__gears_count = gears_count

    def get_door_count(self):
        return self.__door_count
    def set_door_count(self, door_count):
        self.__door_count = door_count

    def get_body_type(self):
        return self.__body_type
    def set_body_type(self, body_type):
        self.__body_type = body_type

    def get_options(self):
        return self.__options
    def set_options(self, options):
        self.__options = options

    def get_gears_count(self):
        return self.__gears_count
    def set_gears_count(self, gears_count):
        self.__gears_count = gears_count

    door_count = property(get_door_count, set_door_count)
    body_type = property(get_body_type, set_body_type)
    options = property(get_options, set_options)
    gears_count = property(get_gears_count, set_gears_count)

    def start_engine(self):
        return Vehicle.start_engine(self)

    def test_system(self):
        return Vehicle.test_system(self)

    def move(self, distance):
        return Vehicle.move(self, distance)

    def load_fuel(self, amount):
        return Vehicle.load_fuel(self, amount)

    def load_cargo(self, amount):
        return Vehicle.load_cargo(self, amount)

    def unload_cargo(self, amount):
        return Vehicle.unload_cargo(self, amount)

    def stop(self):
        return Vehicle.stop(self)


class Bicycle(LandVehicle):
    def __init__(self, make: str, model: str, year: int, vin: str, color: str, engine: bool,
                 engine_type: str, max_fuel_volume: int, fuel_consumption: float, max_speed: int,
                 weight: int, payload: float, warranty_period: int, autopilot: bool,
                 axles_count: int, wheels_count: int,
                 equipment: list):
        LandVehicle.__init__(self, make, model, year, vin, color, engine, engine_type, max_fuel_volume,
                             fuel_consumption, max_speed, weight, payload, warranty_period, autopilot,
                             axles_count, wheels_count)
        self.__equipment = equipment

    def get_equipment(self):
        return self.__equipment
    def set_equipment(self, equipment):
        self.__equipment = equipment

    equipment = property(get_equipment, set_equipment)

    def move(self, distance):
        print('Садимся на велосипед.')
        if self.engine and self.start_engine():
            start = 0
            part = distance / 5
            if part < 100:
                part_consumption = 100 / part
                consumption = self.fuel_consumption / part_consumption
            elif part == 100:
                consumption = self.fuel_consumption
            else:
                multiplier = part // 100
                ostatok = part % 100
                if ostatok:
                    ostatok = 100 / ostatok
                consumption = self.fuel_consumption * multiplier + ostatok
            while start < distance:
                driving = input('Нажимайте Энтер для движения! Или введите "stop" если нужно остановиться')
                if driving == 'stop':
                    self.stop()
                    break
                start += part
                self.fuel_quantity -= consumption
                if self.fuel_quantity < self.max_fuel_volume / 5:
                    if self.fuel_quantity <= 0:
                        self.fuel_quantity = 0
                        print('Топливо закончилось, переходим на педали!')
                        break
                    print(f'Внимание осталось {self.fuel_quantity} литров топлива. Пополните топливо!')
                print(f'Вы проехали {start} км!')
                if start >= distance - 0.5:
                    print(f'Вы на месте!')
                    break
        if not self.engine:
            print('Крутим педали!')
            start = 0
            part = distance / 5
            while start < distance:
                driving = input('Нажимайте Энтер для движения! Или введите "stop" если нужно остановиться')
                if driving == 'stop':
                    self.stop()
                    break
                start += part
                print(f'Вы проехали {start} км!')
                if start >= distance - 0.5:
                    print(f'Вы на месте!')
                    break

    def stop(self):
        print('Нажимаем на тормоза!')
        print('Слазим с велосипеда!')


class RailVehicle(LandVehicle):
    def __init__(self, make, model, year, vin, color, engine, engine_type, max_fuel_volume,
                 fuel_consumption, max_speed, weight, payload, warranty_period, autopilot,
                 rails_width):
        Vehicle.__init__(self, make, model, year, vin, color, engine, engine_type, max_fuel_volume,
                         fuel_consumption, max_speed, weight, payload, warranty_period, autopilot)
        self.__rails_width = rails_width

    def get_rails_width(self):
        return self.__rails_width
    def set_rails_width(self, rails_width):
        self.__rails_width = rails_width

    def move(self, distance):
        return Vehicle.move(self, distance)

    def stop(self):
        return Vehicle.stop(self)

    rails_width = property(get_rails_width, set_rails_width)


class FreightTrain(RailVehicle):
    def __init__(self, make: str, model: str, year: int, vin: str, color: str, engine: bool,
                 engine_type: str, max_fuel_volume: int, fuel_consumption: float, max_speed: int,
                 weight: int, payload: float, warranty_period: int, autopilot: bool, rails_width: int,
                 locomotives_count: int, max_carts_count: int, carts_count: int):
        RailVehicle.__init__(self, make, model, year, vin, color, engine, engine_type, max_fuel_volume,
                             fuel_consumption, max_speed, weight, payload, warranty_period, autopilot,
                             rails_width)
        self.__locomotives_count = locomotives_count
        self.__max_carts_count = max_carts_count
        self.__carts_count = carts_count

    def get_locomotives_count(self):
        return self.__locomotives_count
    def set_locomotives_count(self, locomotives_count):
        self.__locomotives_count = locomotives_count

    def get_max_carts_count(self):
        return self.__max_carts_count
    def set_max_carts_count(self, max_carts_count):
        self.__max_carts_count = max_carts_count

    def get_carts_count(self):
        return self.__carts_count
    def set_carts_count(self, carts_count):
        self.__carts_count = carts_count

    locomotives_count = property(get_locomotives_count, set_locomotives_count)
    max_carts_count = property(get_max_carts_count, set_max_carts_count)
    carts_count = property(get_carts_count, set_carts_count)

    def load_cargo(self, amount):
        print(f'Грузоподъемность поезда равна: {self.payload}.')
        if self.payload >= amount:
            print('Подъезжаем к месту погрузки.\nОткрываем погрузочный люк!')
            self.payload -= amount
            print(f'Осторожно! Погрузчик загружает груз {amount} кг.\nОсторожно! Закрываем погрузочный люк!')
        else:
            print(f"Нельзя загрузить {amount} кг.\n")

    def unload_cargo(self, amount):
        weight_cargo = self.max_weight - self.weight - self.payload
        if amount <= weight_cargo:
            self.payload += amount
            print(f'Подъезжаем к месту разгрузки.\nОткрываем погрузочный люк!')
            weight_cargo -= amount
            print(f'Выгружаем груз {amount} кг.\nОсторожно! Закрываем погрузочный люк!')
        else:
            print(f'Нет столько груза! Транспорт загружен на: {weight_cargo} кг.')


class Railcar(RailVehicle):
    def __init__(self, make: str, model: str, year: int, vin: str, color: str, engine: bool,
                 engine_type: str, max_fuel_volume: int, fuel_consumption: float, max_speed: int,
                 weight: int, payload: float, warranty_period: int, autopilot: bool, rails_width: int,
                 max_number_team: int):
        RailVehicle.__init__(self, make, model, year, vin, color, engine, engine_type, max_fuel_volume,
                             fuel_consumption, max_speed, weight, payload, warranty_period, autopilot,
                             rails_width)
        self.__max_number_team = max_number_team

    def get_max_number_team(self):
        return self.__max_number_team
    def set_max_number_team(self, max_number_team):
        self.__max_number_team = max_number_team

    max_number_team = property(get_max_number_team, set_max_number_team)

    def move(self, distance):
        print('Усаживаемся на дрезину.')
        start = 0
        part = distance / 5
        while start < distance:
            driving = input('Нажимайте Энтер для движения! Или введите "stop" если нужно остановиться')
            print('Двигаем рычаги!')
            if driving == 'stop':
                self.stop()
                break
            start += part
            print(f'Вы проехали {start} км!')
            if start >= distance - 0.5:
                print(f'Вы на месте!')
                break

    def stop(self):
        print('Нажимаем на тормоза!')
        print('Дрязина остановлена!')


class AirVehicle(Vehicle):
    def __init__(self, make, model, year, vin, color, engine, engine_type, max_fuel_volume,
                 fuel_consumption, max_speed, weight, payload, warranty_period, autopilot,
                 seats_count, wings_count, engine_count, max_altitude, max_runway):
        Vehicle.__init__(self, make, model, year, vin, color, engine, engine_type, max_fuel_volume,
                         fuel_consumption, max_speed, weight, payload, warranty_period, autopilot)
        self.__seats_count = seats_count
        self.__wings_count = wings_count
        self.__engine_count = engine_count
        self.__max_altitude = max_altitude
        self.__max_runway = max_runway

    def get_seats_count(self):
        return self.__seats_count
    def set_seats_count(self, seats_count):
        self.__seats_count = seats_count

    def get_wings_count(self):
        return self.__wings_count
    def set_wings_count(self, wings_count):
        self.__wings_count = wings_count

    def get_engine_count(self):
        return self.__engine_count
    def set_engine_count(self, engine_count):
        self.__engine_count = engine_count

    def get_max_altitude(self):
        return self.__max_altitude
    def set_max_altitude(self, max_altitude):
        self.__max_altitude = max_altitude

    def get_max_runway(self):
        return self.__max_runway
    def set_max_runway(self, max_runway):
        self.__max_runway = max_runway

    seats_count = property(get_seats_count, set_seats_count)
    wings_count = property(get_wings_count, set_wings_count)
    engine_count = property(get_engine_count, set_engine_count)
    max_altitude = property(get_max_altitude, set_max_altitude)
    max_runway = property(get_max_runway, set_max_runway)

    def move(self, distance):
        if self.start_engine():
            start = 0
            part = distance / 5
            if part < 100:
                part_consumption = 100 / part
                consumption = self.fuel_consumption / part_consumption
            elif part == 100:
                consumption = self.fuel_consumption
            else:
                multiplier = part // 100
                ostatok = part % 100
                if ostatok:
                    ostatok = 100 / ostatok
                consumption = self.fuel_consumption * multiplier + ostatok
            while start < distance:
                driving = input('Нажимайте Энтер для полета! Или введите "stop" если нужно остановиться')
                if driving == 'stop':
                    self.stop()
                    break
                start += part
                self.fuel_quantity -= consumption
                if self.fuel_quantity < self.max_fuel_volume / 5:
                    if self.fuel_quantity <= 0:
                        self.fuel_quantity = 0
                        print('Топливо кончилось, вы скорее всего разбились!')
                        break
                    print(f'Внимание осталось {self.fuel_quantity} литров топлива. Пополните топливо!')
                print(f'Вы пролетели {start} км!')
                if start >= distance - 0.5:
                    print('Вы на месте!')
                    break

    def stop(self):
        print('Вы остановились!')


class AirPlane(AirVehicle, LandVehicle):
    def __init__(self, make: str, model: str, year: int, vin: str, color: str, engine: bool, engine_type: str,
                 max_fuel_volume: int, fuel_consumption: float, max_speed: int, weight: int, payload: float,
                 warranty_period: int, autopilot: bool, axles_count: int, wheels_count: int,
                 seats_count: int, wings_count: int, engine_count: int, max_altitude: int, max_runway: int,
                 class_type: str, runway_type: str, entrance_count: int):
        AirVehicle.__init__(self, make, model, year, vin, color, engine, engine_type, max_fuel_volume,
                            fuel_consumption, max_speed, weight, payload, warranty_period, autopilot,
                            wings_count, engine_count, max_altitude, seats_count, max_runway)
        LandVehicle.__init__(self, make, model, year, vin, color, engine, engine_type, max_fuel_volume,
                             fuel_consumption, max_speed, weight, payload, warranty_period, autopilot,
                             axles_count, wheels_count)
        self.__class_type = class_type
        self.__runway_type = runway_type
        self.__entrance_count = entrance_count

    def get_class_type(self):
        return self.__class_type
    def set_class_type(self, class_type):
        self.__class_type = class_type

    def get_max_runway(self):
        return self.__max_runway
    def set_max_runway(self, max_runway):
        self.__max_runway = max_runway

    def get_runway_type(self):
        return self.__runway_type
    def set_runway_type(self, runway_type):
        self.__runway_type = runway_type

    def get_entrance_count(self):
        return self.__entrance_count
    def set_entrance_count(self, entrance_count):
        self.__entrance_count = entrance_count

    class_type = property(get_class_type, set_class_type)
    runway_type = property(get_runway_type, set_runway_type)
    entrance_count = property(get_entrance_count, set_entrance_count)

    def test_system(self):
        return AirVehicle.test_system(self)

    def start_engine(self):
        return AirVehicle.test_system(self)

    def take_off(self):
        if self.start_engine():
            print('Выезжаем на взлетную полосу!\nНабираем скорость!\nВзлетаем!\nУбираем шасси!')

    def move(self, distance):
        return AirVehicle.move(self, distance)

    def land(self):
        print('Заходим на посадку!\nВыдвигаем шасси\nСнижаем скорость!\nПриземляемся!\nЕдем в место стоянки!')
        return True

    def stop(self):
        print('Вы остановились!')


class Helicopter(AirVehicle, LandVehicle):
    def __init__(self, make: str, model: str, year: int, vin: str, color: str, engine: bool, engine_type: str,
                 max_fuel_volume: int, fuel_consumption: float, max_speed: int, weight: int, payload: float,
                 warranty_period: int, autopilot: bool, axles_count: int, wheels_count: int,
                 seats_count: int, wings_count: int, engine_count: int, max_altitude: int, max_runway: int,
                 cargo_entrance: bool):
        AirVehicle.__init__(self, make, model, year, vin, color, engine, engine_type, max_fuel_volume,
                            fuel_consumption, max_speed, weight, payload, warranty_period, autopilot,
                            seats_count, wings_count, engine_count, max_altitude, max_runway)
        LandVehicle.__init__(self, make, model, year, vin, color, engine, engine_type, max_fuel_volume,
                             fuel_consumption, max_speed, weight, payload, warranty_period, autopilot,
                             axles_count, wheels_count)
        self.__cargo_entrance = cargo_entrance

    def get_passengers_count(self):
        return self.__passengers_count
    def set_passengers_count(self, passengers_count):
        self.__passengers_count = passengers_count

    def get_max_runway(self):
        return self.__max_runway
    def set_max_runway(self, max_runway):
        self.__max_runway = max_runway

    def get_cargo_entrance(self):
        return self.__cargo_entrance
    def set_cargo_entrance(self, cargo_entrance):
        self.__cargo_entrance = cargo_entrance

    cargo_entrance = property(get_cargo_entrance, set_cargo_entrance)

    def test_system(self):
        return AirVehicle.test_system(self)

    def start_engine(self):
        return AirVehicle.test_system(self)

    def take_off(self):
        if self.start_engine():
            print('Выезжаем на взлетную полосу!\nНабираем скорость!\nВзлетаем!\nУбираем шасси!')

    def move(self, distance):
        return AirVehicle.move(self, distance)

    def land(self):
        print('Заходим на посадку!\nВыдвигаем шасси\nСнижаем скорость!\nПриземляемся!\nЕдем в место стоянки!')

    def stop(self):
        print('Вы остановились!')


class WaterVehicle(Vehicle):
    def __init__(self, make, model, year, vin, color, engine, engine_type, max_fuel_volume,
                 fuel_consumption, max_speed, weight, payload, warranty_period, autopilot,
                 displacement, under_water_support, engine_count):
        Vehicle.__init__(self, make, model, year, vin, color, engine, engine_type, max_fuel_volume,
                         fuel_consumption, max_speed, weight, payload, warranty_period, autopilot)
        self.__displacement = displacement
        self.__under_water_support = under_water_support
        self.__engine_count = engine_count

    def get_displacement(self):
        return self.__displacement
    def set_displacement(self, displacement):
        self.__displacement = displacement

    def get_under_water_support(self):
        return self.__under_water_support
    def set_under_water_support(self, under_water_support):
        self.__under_water_support = under_water_support

    def get_engine_count(self):
        return self.__engine_count
    def set_engine_count(self, engine_count):
        self.__engine_count = engine_count

    displacement = property(get_displacement, set_displacement)
    under_water_support = property(get_under_water_support, set_under_water_support)
    engine_count = property(get_engine_count, set_engine_count)

    def test_system(self):
        return Vehicle.test_system(self)

    def start_engine(self):
        return Vehicle.start_engine(self)

    def move(self, distance):
        if self.start_engine():
            start = 0
            part = distance / 5
            if part < 100:
                part_consumption = 100 / part
                consumption = self.fuel_consumption / part_consumption
            elif part == 100:
                consumption = self.fuel_consumption
            else:
                multiplier = part // 100
                ostatok = part % 100
                if ostatok:
                    ostatok = 100 / ostatok
                consumption = self.fuel_consumption * multiplier + ostatok
            while start < distance:
                driving = input('Нажимайте Энтер для плавания! Или введите "stop" если нужно остановиться')
                if driving == 'stop':
                    self.stop()
                    break
                start += part
                self.fuel_quantity -= consumption
                if self.fuel_quantity < self.max_fuel_volume / 5:
                    if self.fuel_quantity <= 0:
                        self.fuel_quantity = 0
                        print('Топливо кончилось, дальше вплавь!')
                        break
                    print(f'Внимание осталось {self.fuel_quantity} литров топлива. Пополните топливо!')
                print(f'Вы проплыли {start} км!')
                if start >= distance - 0.5:
                    print('Вы на месте!')
                    break

    def stop(self):
        return Vehicle.stop(self)


class JetSki(WaterVehicle):
    def __init__(self, make: str, model: str, year: int, vin: str, color: str, engine: bool, engine_type: str,
                 max_fuel_volume: int, fuel_consumption: float, max_speed: int, weight: int, payload: float,
                 warranty_period: int, autopilot: bool, displacement: int, under_water_support: bool, engine_count: int,
                 equipment: list):
        WaterVehicle.__init__(self, make, model, year, vin, color, engine, engine_type, max_fuel_volume,
                              fuel_consumption, max_speed, weight, payload, warranty_period, autopilot,
                              displacement, under_water_support, engine_count)
        self.__equipment = equipment

    def get_equipment(self):
        return self.__equipment
    def set_equipment(self, equipment):
        self.__equipment = equipment

    equipment = property(get_equipment, set_equipment)

    def test_system(self):
        return WaterVehicle.test_system(self)

    def start_engine(self):
        return WaterVehicle.start_engine(self)

    def move(self, distance):
        return WaterVehicle.move(self, distance)

    def stop(self):
        return WaterVehicle.stop(self)


if __name__ == '__main__':
    mers = Car('mers', 'a180', 2015, 'WDD14244667678334', 'black', True, '1.5 CDI',
               55, 4.5, 260, 1500, 400, 5, False, 2, 4, 5, 'hech', ['op1', 'op2'], 6)
    mers.set_year(2022)
    mers.test_system()
    mers.start_engine()
    mers.move(6)
    mers.load_fuel(20)
    mers.load_cargo(399)
    mers.unload_cargo(99)

    aist = Bicycle('aist', 'black', 2021, 'WDD14244667678334', 'black', False, '',
                   0, 0, 60, 15, 120, 3, False, 2, 2, ['eq1', 'eq2'])
    aist.test_system()
    aist.start_engine()
    aist.move(6)
    aist.move(30)
    aist.load_fuel(20)

    ft = FreightTrain('FT', 'FT1000', 2016, 'WDD14244667678334', 'green', True,
                      '20.0 дизельный', 1000, 60, 120, 1000, 2000, 5, True,
                      100, 2, 70, 40)
    ft.test_system()
    ft.start_engine()
    ft.move(6)
    ft.move(30)
    ft.load_fuel(20)

    rlc = Railcar('RC', 'RC2000', 2017, 'WDD14244667678334', 'brown', False,
                      '', 0, 0, 40, 1000, 2000, 5, False,
                      100, 4)
    rlc.test_system()
    rlc.start_engine()
    rlc.move(6)
    rlc.move(30)
    rlc.load_fuel(20)

    airbus = AirPlane('airbus', 'a100', 2020, 'WDD14244667678334', 'white', True,
                      '1000superjet', 50, 1, 800, 30, 10, 5, True, 8, 16, 300, 2, 4,
                      3000, 3000, 'passenger', 'road', 3)
    airbus.test_system()
    airbus.start_engine()
    airbus.move(6)
    airbus.move(30)
    airbus.load_fuel(20)

    hlc = Helicopter('hel', 'abc', 2013, 'WDD14244667678334', 'black', True, '10.0 CDI',
                     1000, 100, 350, 10, 5, 5, True, 2, 3, 10, 0, 1, 2000, 1000, False)
    hlc.test_system()
    hlc.start_engine()
    hlc.move(6)
    hlc.move(30)
    hlc.load_fuel(20)

    js = JetSki('JTS', 't34', 2019, 'WDD14244667678334', 'red', True, '2.0 бенз', 20, 3,
                90, 200, 300, 5, False, 1, False, 1, ['eq1', 'eq2'])
    js.test_system()
    js.start_engine()
    js.move(6)
    js.move(30)
    js.load_fuel(20)
