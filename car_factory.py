from car import Car

# import engines
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

# import batteries
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

# importing tires
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class CarFactory:
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tires_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        tires = CarriganTires(tires_array)
        car = Car(battery, engine, tires)

        return car
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tires_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        tires = OctoprimeTires(tires_array)
        car = Car(battery, engine, tires)

        return car

    def create_palindrome(current_date, last_service_date, warning_light_on, tires_array):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date)
        tires = CarriganTires(tires_array)
        car = Car(battery, engine, tires)

        return car

    def create_rarschach(current_date, last_service_date, current_mileage, last_service_mileage, tires_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        tires = OctoprimeTires(tires_array)
        car = Car(battery, engine, tires)

        return car

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tires_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        tires = CarriganTires(tires_array)
        car = Car(battery, engine, tires)

        return car
