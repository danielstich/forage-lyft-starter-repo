import unittest

from tires.carrigan_tire import CarriganTire

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

if __name__ == '__main__':
  unittest.main()