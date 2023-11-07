import sys
import unittest
from datetime import datetime

sys.path.insert(1, './')

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

# testing nubbin battery
class TestNubbin(unittest.TestCase):
    # battery has expired, needs to be serviced
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(last_service_date)

        self.assertTrue(battery.needs_service())

    # battery has not expired, does not need to be serviced
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = NubbinBattery(last_service_date)

        self.assertFalse(battery.needs_service())

# testing spindler battery
class TestSpindler(unittest.TestCase):
    # battery has expired, needs to be serviced
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        battery = SpindlerBattery(last_service_date)

        self.assertTrue(battery.needs_service())

    # battery has not expired, does not need to be serviced
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = SpindlerBattery(last_service_date)

        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()