from operator import truediv
from .tire import Tire

class CarriganTire(Tire):
  def __init__(self, worn_array):
    super().__init__()
    self.worn_array = worn_array

  def needs_service(self):
    for tire_word_indicator in self.worn_array:
      if tire_word_indicator >= .9:
        return True
    return False