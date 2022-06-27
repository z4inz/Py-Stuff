import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    print(kwargs)
    for key in kwargs:
      for i in range(kwargs[key]):
        self.contents.append(key)

  def draw(self, balls):
    draw_list = list()
    if balls > len(self.contents):
      return self.contents
    for i in range(balls):
      idx = random.randrange(len(self.contents))
      draw_list.append(self.contents[idx])
      self.contents.pop(idx)
    return draw_list
      

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for i in range(num_experiments):
    expected_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    colours_recieved = hat_copy.draw(num_balls_drawn)

    for colour in colours_recieved:
      if(colour in expected_copy):
        expected_copy[colour] -= 1

    if all(value <= 0 for value in expected_copy.values()):
      M += 1
      
  return M/num_experiments
      

