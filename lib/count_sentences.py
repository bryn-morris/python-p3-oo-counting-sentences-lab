#!/usr/bin/env python3
import re
import ipdb

class MyString:
  
  def __init__(self, value = "sample"):
    self.value = value

  def value_getter(self):
    return self._value
  
  def value_setter(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return self.value.count(".") > 0
  
  def is_question(self):
    return self.value.count("?") > 0
  
  def is_exclamation(self):
    return self.value.count("!") > 0
  
  def count_sentences(self):

    var = re.split(r"[!.?]",self.value.strip())

    print(f"Starting List: {var}")

    # list comprehension approach
    # new_list = [var.remove(indexVal) for indexVal in var if indexVal == ""]


    #This is only firing once but ONLY when .remove is called?
    # n = 1
    # for indexVal in var:
    #   if indexVal == "":
    #     print(f"How many times is this firing?: {n}")
    #     print(var.index(indexVal))
    #     var.remove(indexVal)
    #     n += 1

    ###########################################################################

    # This while loop works as long as i DON'T increment l with:
          # l += 1

    inc = 0
    while inc < var.count(""):
      
      print (f"How many times is this firing? {inc+1}")
      var.remove("")
      
    print(f"List after removal: {var}")
  
    i = 0
    for eachIndex in var:
      i += 1

    print(f"Count of Indices in list after removal: {i}")

    return i
  

  value = property(value_getter, value_setter)


# instance = MyString("This. Is! A? Sample!.")

# instance.count_sentences()