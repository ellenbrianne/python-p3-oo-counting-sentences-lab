#!/usr/bin/env python3
import re 

class MyString:
    def __init__(self, value=''):
        self.value = value

    def is_sentence(self):
        if self.value.endswith(".") == True:
            return True
        else: 
            return False
    
    def is_question(self):
        if self.value.endswith("?") == True:
            return True
        else: 
            return False
    
    def is_exclamation(self):
        if self.value.endswith("!") == True:
            return True
        else: 
            return False
    
    def count_sentences(self):
        pattern = re.compile(r'[\.\?\!]')
        match = pattern.split(self.value)
        while "" in match:
            match.remove("")
        return len(match)
  
    def get_value(self):
        return self._value
  
    def set_value(self, value):
        if isinstance(value, str):
            self._value = value
        else: 
            print("The value must be a string.")

    value = property(get_value, set_value)

new_string = MyString("This is one. This is two? This is three!")
new_string.count_sentences()