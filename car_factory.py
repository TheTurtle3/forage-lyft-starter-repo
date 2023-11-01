from car import Car

# import engines
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

# import batteries
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

class Calliope(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

        # Engine
        self.engine = CapuletEngine(current_mileage, last_service_mileage)

        # Battery
        self.battery = SpindlerBattery(last_service_date)
    
    def needs_service(self):
        if self.battery.needs_service():
            return True
        elif self.engine.engine_should_be_serviced():
            return True
        else:
            False

class Glissade(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

        # Engine
        self.engine = WilloughbyEngine(current_mileage, last_service_mileage)

        # Battery
        self.battery = SpindlerBattery(last_service_date)
    
    def needs_service(self):
        if self.battery.needs_service():
            return True
        elif self.engine.engine_should_be_serviced():
            return True
        else:
            False

class Palindrome(Car):
    def __init__(self, last_service_date, warning_light_on):
        self.last_service_date = last_service_date
        self.warning_light_on = warning_light_on

        # Engine
        self.engine = SternmanEngine(warning_light_on)

        # Battery
        self.battery = SpindlerBattery(last_service_date)
    
    def needs_service(self):
        if self.battery.needs_service():
            return True
        elif self.engine.engine_should_be_serviced():
            return True
        else:
            False

class Rorschach(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

        # Engine
        self.engine = WilloughbyEngine(current_mileage, last_service_mileage)

        # Battery
        self.battery = NubbinBattery(last_service_date)
    
    def needs_service(self):
        if self.battery.needs_service():
            return True
        elif self.engine.engine_should_be_serviced():
            return True
        else:
            False

class Thovex(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

        # Engine
        self.engine = CapuletEngine(current_mileage, last_service_mileage)

        # Battery
        self.battery = NubbinBattery(last_service_date)
    
    def needs_service(self):
        if self.battery.needs_service():
            return True
        elif self.engine.engine_should_be_serviced():
            return True
        else:
            False