"""progression.py"""

from typing import List, Tuple, Dict
from models.scale import Scale
from models.chord import Chord

class ChordProgression:
    """
    A class to represent a chord progression based on a given musical scale.

    Attributes:
    -----------
    scale : Scale
        The musical scale on which the chord progression is based.

    Methods:
    --------
    generate(progression_pattern):
        Generates a chord progression based on the provided progression pattern.
    
    get_progression_patterns():
        Returns common chord progression patterns based on the type of scale (Major or Minor).
    """
    
    # Define common progression patterns
    PROGRESSION_PATTERNS: Dict[str, List[List[Tuple[int, str]]]] = {
        'major': [
            [(0, 'major'), (3, 'major'), (4, 'major'), (0, 'major')],  # I-IV-V-I
            [(0, 'major'), (4, 'major'), (3, 'major'), (0, 'major')],  # I-V-IV-I
            [(0, 'major'), (1, 'minor'), (4, 'major'), (0, 'major')]   # I-ii-V-I
        ],
        'minor': [
            [(0, 'minor'), (3, 'minor'), (4, 'minor'), (0, 'minor')],  # i-iv-v-i
            [(0, 'minor'), (4, 'minor'), (3, 'minor'), (0, 'minor')],  # i-v-iv-i
            [(0, 'minor'), (1, 'diminished'), (4, 'minor'), (0, 'minor')] # i-ii°-v-i
        ]
    }
    
    def __init__(self, scale: Scale):
        if not isinstance(scale, Scale):
            raise ValueError("Scale must be a Scale object")
        self.__scale = scale
        
    @property
    def scale(self) -> Scale:
        return self.__scale
    
    @property
    def key(self) -> str:
        """Returns the key/tonic of the scale"""
        return self.__scale.key.name
    
    @property
    def scale_type(self) -> str:
        """Returns the type of scale (Major or Minor)"""
        return 'Major' if 'Major' in self.__scale.name else 'Minor' if 'Minor' in self.__scale.name else 'Unknown'
      
    def generate(self, pattern: List[Tuple[int, str]]) -> List[Chord]:
        """Generates a chord progression based on the provided progression pattern."""
        progression = []
        for degree_index, chord_type in pattern:
            if degree_index >= len(self.__scale.degrees):
                raise ValueError(f"Invalid degree index: {degree_index}")
            degree = self.__scale.degrees[degree_index]
            progression.append(Chord(degree.note.name, chord_type))
        return progression
    
    def get_progression_patterns(self) -> List[List[Tuple[int, str]]]:
        """Returns appropriate progression patterns based on scale type"""
        if 'Major' in self.scale.name:
            return self.PROGRESSION_PATTERNS['major']
        elif 'Minor' in self.scale.name:
            return self.PROGRESSION_PATTERNS['minor']
        return [self.PROGRESSION_PATTERNS['major'][0]]  # Default to I-IV-V-I
    
    def __str__(self) -> str:
        return f"ChordProgression for {self.scale.name}"