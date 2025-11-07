class Analyzer:
  def __init__(self, my_list):
    self.my_list = list(my_list)

  def add_number(self, x):
    self.my_list.append(x)
    return self.my_list
  
  def even_count(self):
    even_list = [i for i in self.my_list if i % 2 == 0 ]
    return len(even_list)
  
  def odd_count(self):
    odd_list = [i for i in self.my_list if i % 2 != 0 ]
    return len(odd_list)
  
  def highest_number(self):
    return max(self.my_list)
  
  def increasing_pairs(self):
    count = 0
    for i in range(1, len(self.my_list)):
        if self.my_list[i] > self.my_list[i - 1]:
            count += 1
    return count

  

