"""
THE NOTE CLASS
Represents a musical note with name and key attributes
"""

from typing import Optional

class Note:
    """
    A class to represent a musical note.
    
    Attributes:
        _name (str): The name of the note (private)
        _key (str): The key of the note (private)
        
    Properties:
        name: Get/set the note name with validation
        key: Get/set the note key with validation
    """
    VALID_NOTES = {'A', 'B', 'C', 'D', 'E', 'F', 'G',
                   'Ab', 'Bb', 'Db', 'Eb', 'Gb', 'F#', 'G#'}
    
    def __init__(self, name: str, key: str):
        """
        Initialize a Note instance with validation.

        Args:
            name: The name of the note
            key: The key of the note
            
        Raises:
            ValueError: If name or key is invalid
        """
        self.__name = None
        self.__key = None
        self.name = name
        self.key = key
        
    @property
    def name(self) -> str:
        """Get the name of the note."""
        return self.__name
   
    @name.setter
    def name(self, value: str) -> None:
        """
        Set the note name with validation.
        
        Args:
            value: The name to set
            
        Raises:
            ValueError: If the note name is invalid
        """
        if not value or not isinstance(value, str):
            raise ValueError("Note name must be a non-empty string")
        if value not in self.VALID_NOTES:
            raise ValueError(f"Invalid note name: {value}")
        self.__name = value
        
    @property
    def key(self) -> str:
        """Get the key of the note."""
        return self.__key
    
    @key.setter
    def key(self, value: str) -> None:
        """
        Set the note key with validation.
        
        Args:
            value: The key to set
            
        Raises:
            ValueError: If the key is invalid
        """
        if not value or not isinstance(value, str):
            raise ValueError("Note key must be a non-empty string")
        if value not in self.VALID_NOTES:
            raise ValueError(f"Invalid note key: {value}")
        self._key = value
    
    def __str__(self) -> str:
        """String representation of the note"""
        return f"{self.name}"
    
    def __repr__(self) -> str:
        """Detailed string representation of the note"""
        return f"Note(name='{self.name}', key='{self.key}')"
    
    def __eq__(self, other: Optional['Note']) -> bool:
        """
        Compare two notes for equality.
        
        Args:
            other: Another Note instance to compare with
            
        Returns:
            bool: True if notes are equal, False otherwise
        """
        if not isinstance(other, Note):
            return False
        return self.name == other.name and self.key == other.key
