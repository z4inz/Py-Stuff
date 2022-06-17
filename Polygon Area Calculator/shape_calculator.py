class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.dots = ""

  def __str__(self):
    details = "Rectangle" + "(width=" + str(self.width) + ", " + "height=" + str(self.height) + ")"
    return details

  def set_width(self, width):
    self.width = width
  
  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width*self.height

  def get_perimeter(self):
    return self.width * 2 + self.height * 2

  def get_diagonal(self):
    return ((self.width)**2 + (self.height)**2)**0.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    for x in range(self.height):
      self.dots = self.dots + "*" * self.width + "\n"  
    return self.dots

  def get_amount_inside(self, name):
    return self.get_area()//name.get_area()
  

class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side
    self.dots = ""

  def set_side(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    details = "Square" + "(side=" + str(self.width) + ")"
    return details

  def set_width(self, width):
    return self.set_side(width)

  def set_height(self, height):
    return self.set_side(height)