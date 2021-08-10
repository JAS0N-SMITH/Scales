"""
THE DEGREE FILE
a degree is a note?
how many? C,Db,D,Eb,E,F,Gb,G,Ab,A,Bb,B
"""


class Degree:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def assign_note(self, note):
        self.note = note
