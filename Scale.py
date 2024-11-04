"""
THE SCALE FILE
"""

from Chord import Chord

class Scale:
    def __init__(self, name, key, degrees):
        self.name = name
        self.key = key
        self.degrees = degrees

    def display(self):
        return f"Scale: {self.name}, Key: {self.key}, Degrees: {self.degrees}"
