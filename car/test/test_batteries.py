import unittest
from datetime import datetime

from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery

class TestNubbinBattery(unittest.TestCase):
  def test_nubbin_battery_should_be_serviced(self):
    today = datetime.today().date()
    last_service_date = today.replace(year = today.year - 5)

    battery = NubbinBattery(last_service_date, today)
    self.assertTrue(battery.needs_service())

  def test_nubbin_battery_should_not_be_serviced(self):
    today = datetime.today().date()
    last_service_date = today.replace(year = today.year - 3)

    battery = NubbinBattery(last_service_date, today)
    self.assertFalse(battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):
  def test_spindler_battery_should_be_serviced(self):
    today = datetime.today().date()
    last_service_date = today.replace(year = today.year - 4)

    battery = SpindlerBattery(last_service_date, today)
    self.assertTrue(battery.needs_service())

  def test_spindler_battery_should_not_be_serviced(self):
    today = datetime.today().date()
    last_service_date = today.replace(year = today.year - 2)

    battery = SpindlerBattery(last_service_date, today)
    self.assertFalse(battery.needs_service())

if __name__ == '__main__':
  unittest.main()