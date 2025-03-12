from typing import List
from models.degree import Degree
from models.note import Note

class Scale:
    """A class representing a musical scale.
    
    Attributes:
        name (str): The name of the scale (e.g. "C Major Scale")
        key (Note): The root note/key of the scale
        degrees (List[Degree]): The ordered list of scale degrees
        
    Properties:
        root_note: The tonic/first note of the scale
        notes: List of all notes in the scale
    """
    
    def __init__(self, name: str, key: Note, degrees: List[Degree]):
        if not name or not isinstance(name, str):
            raise ValueError("Scale name must be a non-empty string")
        if not isinstance(key, Note):
            raise ValueError("Key must be a Note object")
        if not degrees or not isinstance(degrees, list):
            raise ValueError("Degrees must be a non-empty list")
            
        self.__name = name
        self.__key = key
        self.__degrees = degrees
        
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def key(self) -> Note:
        return self.__key
    
    @property
    def degrees(self) -> List[Degree]:
        return self.__degrees
    
    @property
    def root_note(self) -> Note:
        """returns the tonic/first note of the scale"""
        return self.degrees[0].__note
    
    @property
    def notes(self) -> List[Note]:
        """returns a list of all notes in the scale"""
        return [degree.__note for degree in self.degrees]
    
    def __str__(self) -> str:
        return f"{self.__name} Scale"
    
    def __repr__(self) -> str:
        return f"Scale(name={self.__name}, key={self.__key}, degrees={self.__degrees})"
