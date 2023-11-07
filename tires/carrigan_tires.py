from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tires_array):
        self.tires_array = tires_array

    def needs_service(self):
        return max(self.tires_array) >= 0.9