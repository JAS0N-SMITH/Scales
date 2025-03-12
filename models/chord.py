from typing import Optional
from models.note import Note

class Chord:
    """A class representing a musical chord.
    
    Attributes:
        root_note (Note): The root note of the chord
        chord_type (str): The type of chord (major, minor, diminished, etc.)
        
    Properties:
        name: The full name of the chord (e.g. "C major")
    """
    
    VALID_TYPES = {'major', 'minor', 'diminished', 'augmented', 
                   'major7', 'minor7', 'dominant7'}
    
    def __init__(self, root_note, chord_type):
        """
        
        """
        if not isinstance(root_note, str):
            raise ValueError("Root note must be a Note object")
        if not isinstance(chord_type, str):
            raise ValueError("Chord type must be a string")
        if chord_type.lower() not in self.VALID_TYPES:
            raise ValueError(f"Invalid chord type: {chord_type}")
        
        
        self.__root_note = root_note
        self.__chord_type = chord_type.lower()
        
    @property
    def root_note(self) -> Note:
        return self.__root_note
    
    @property
    def chord_type(self) -> str:
        return self.__chord_type
    
    @property
    def name(self) -> str:
        return f"{self.__root_note} {self.__chord_type}"
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f"Chord(root_note={self.__root_note}, chord_type={self.__chord_type})"
    
    def __eq__(self, other: Optional['Chord']) -> bool:
        if not isinstance(other, Chord):
            return False
        return self.root_note == other.root_note and self.chord_type == other.chord_type