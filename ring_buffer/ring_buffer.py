class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
  
  def append(self, item):
    self.storage[self.current] = item
    if self.current < len(self.storage)-1:
      self.current = self.current+1
    else:
      self.current = 0

  def get(self):
    new = []
    for i in range (self.capacity):
      if self.storage[i]:
        new.append(self.storage[i])
    return new
      


