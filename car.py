from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, battery, engine, tires):
        self.battery = battery
        self.engine = engine
        self.tires = tires

    def needs_service(self):
        return self.battery.needs_serivce() or self.engine.needs_service() or self.tires.needs_service()
