from lib2to3.pgen2.tokenize import untokenize
import unittest

from engines.capulet_engine import CapuletEngine
from engines.willoughby_engine import WilloughbyEngine
from engines.sternman_engine import SternmanEngine

class TestCapuletEngine(unittest.TestCase):
  def test_capulate_engine_needs_serviced(self):
    current_mileage = 30001
    last_service_mileage = 0
    engine = CapuletEngine(current_mileage, last_service_mileage)
    self.assertTrue(engine.needs_service())

  def test_capulate_engine_doesnt_need_serviced(self):
    current_mileage = 29999
    last_service_mileage = 0
    engine = CapuletEngine(current_mileage, last_service_mileage)
    self.assertFalse(engine.needs_service())  

class TestWilloughbyEngine(unittest.TestCase):
  def test_willoughby_engine_needs_serviced(self):
    current_mileage = 60001
    last_service_mileage = 0
    engine = WilloughbyEngine(current_mileage, last_service_mileage)
    self.assertTrue(engine.needs_service())

  def test_willoughby_engine_doesnt_need_serviced(self):
    current_mileage = 59999
    last_service_mileage = 0
    engine = WilloughbyEngine(current_mileage, last_service_mileage)
    self.assertFalse(engine.needs_service())  

class TestStermanEngine(unittest.TestCase):
  def test_sterman_engine_needs_serviced(self):
    warning_light = True
    engine = SternmanEngine(warning_light)

    self.assertTrue(engine.needs_service())

  def test_sterman_engine_doesnt_need_serviced(self):
    warning_light = False
    engine = SternmanEngine(warning_light)

    self.assertFalse(engine.needs_service())

if __name__ == '__main__':
  unittest.main()