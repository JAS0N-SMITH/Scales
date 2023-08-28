"""
THE DEGREE FILE
a degree is a note?
how many? C,Db,D,Eb,E,F,Gb,G,Ab,A,Bb,B
"""


class Degree:
    """name: the name of the degree, symbol: the symbol of the degree"""
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.note = None

    def assign_note(self, note):
        """assigns a note to the degree"""
        self.note = note
