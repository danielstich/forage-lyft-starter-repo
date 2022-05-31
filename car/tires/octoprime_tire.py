from .tire import Tire

class OctoprimeTire(Tire):
  def __init__(self, worn_array):
    super().__init__()
    self.worn_array = worn_array

  def needs_service(self):
    sum = 0
    for tire_worn_indicator in self.worn_array:
      sum = sum + tire_worn_indicator
    if sum >= 3:
      return True
    else: 
      return False