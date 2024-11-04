"""
THE DEGREE FILE
a degree is a note?
how many? C,Db,D,Eb,E,F,Gb,G,Ab,A,Bb,B
"""


class Degree:
    """name: the name of the degree, symbol: the symbol of the degree"""
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol
        self.note = None

    def assign_note(self, note: str):
            """assigns a note to the degree"""
            self.note = note
    def __repr__(self):
        return f"Degree(name={self.name}, symbol={self.symbol}, note={self.note})"
