import sys
import unittest

sys.path.insert(1, './')

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

# testing carrigan tires
class TestCarrigan(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tires_array = [.9,0,0,.5]
        tires = CarriganTires(tires_array)

        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tires_array = [.8,.7,0,.5]
        tires = CarriganTires(tires_array)

        self.assertFalse(tires.needs_service())

# testing octoprime tires
class TestOctoprime(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tires_array = [.9,.9,.9,.5]
        tires = OctoprimeTires(tires_array)

        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tires_array = [.9,0,.1,.5]
        tires = OctoprimeTires(tires_array)

        self.assertFalse(tires.needs_service())

if __name__ == '__main__':
    unittest.main()