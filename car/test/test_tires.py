import unittest

from tires.carrigan_tire import CarriganTire
from tires.octoprime_tire import OctoprimeTire

# Carrigan Tire Tests
class TestCarriganTire(unittest.TestCase):
  # Test if all tires are worn
  def test_carrigan_tires_all_are_worn(self):
    worn_array = [.9, .9, .9, .9]

    tires = CarriganTire(worn_array)

    self.assertTrue(tires.needs_service())

  # Test if one tire is worn
  def test_carrigan_tires_one_is_worn(self):
    worn_array = [0, .89, .89, .9]
    tires = CarriganTire(worn_array)

    self.assertTrue(tires.needs_service())

  # Test if no tires are worn
  def test_carrigan_tires_none_are_worn(self):
    worn_array = [0, 0, .2, .4]
    tires = CarriganTire(worn_array)

    self.assertFalse(tires.needs_service())

# Octoprime Tire Tests
class TestOctoprimeTire(unittest.TestCase):
  # Test if sum of worn tires is greater than 3
  def test_octoprime_tires_sum_greater_than_three(self):
    worn_array = [.7, .8, .7, .8]
    tires = OctoprimeTire(worn_array)

    self.assertTrue(tires.needs_service())

  # Test if sum of worn tires is less than 3
  def test_octoprime_tires_sum_less_than_three(self):
    worn_array = [.9, .9, .1, 0]
    tires = OctoprimeTire(worn_array)

    self.assertFalse(tires.needs_service())

if __name__ == '__main__':
  unittest.main()