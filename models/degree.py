"""
THE DEGREE FILE
a degree is a note?
how many? C,Db,D,Eb,E,F,Gb,G,Ab,A,Bb,B
"""

from typing import Optional
from models.note import Note

class Degree:
    """A class representing a scale degree.
    
    Attributes:
        name (str): The name of the degree (First, Second, etc.)
        symbol (str): The roman numeral symbol (I, II, etc.)
        note (Note): The note assigned to this degree
    """
    
    VALID_SYMBOLS = {'I', 'II', 'III', 'IV', 'V', 'VI', 'VII',
                     'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii'}
    
    def __init__(self, name: str, symbol: str):
        if not name or not isinstance(name, str):
            raise ValueError("Degree name must be a non-empty string")
        if not symbol or symbol not in self.VALID_SYMBOLS:
            raise ValueError(f"Invalid degree symbol: {symbol}")
        
        self.__name = name
        self.__symbol = symbol
        self.__note = Optional[Note] = None
        
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def symbol(self) -> str:
        return self.__symbol
    
    @property
    def note(self) -> Optional[Note]:
        return self.__note
    
    def assign_note(self, note: Note) -> None:
        """assigns a note to the degree"""
        if not isinstance(note, Note):
            raise ValueError("Note must be a Note object")
        self.__note = note
        
    def __str__(self) -> str:
        note_str = self.note.name if self.note else "unassigned"
        return f"{self.symbol} ({note_str})"
        
    def __repr__(self) -> str:
        return f"Degree(name={self.__name}, symbol={self.__symbol}, note={self.__note})"
