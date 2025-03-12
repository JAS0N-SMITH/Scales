"""Scale Factory"""

from models.scale import Scale
from models.note import Note
from models.degree import Degree
from config.scale_options import scale_options_dict

class ScaleFactory:
    """
    A factory class for creating musical scales.
    Methods
    -------
    create_scale(name: str, key: Note, degrees: list[Degree]) -> Scale
        Create a scale object with the given name, key, and degrees.
    create_from_pattern(scale_name: str, notes: list[Note], degrees: list[Degree]) -> Scale
        Create a scale from a pattern defined in the scale_options_dict.
    """
    @staticmethod
    def create_scale(name: str, key: Note, degrees: list[Degree]) -> Scale:
        """Create a scale object"""
        return Scale(f"{key.name} {name}", key, degrees)
    
    @staticmethod
    def create_from_pattern(scale_name: str, notes: list[Note], degrees: list[Degree]) -> Scale:
        """Create a scale from a pattern in scale_options_dict"""
        scale_info = scale_options_dict.get(scale_name)
        if not scale_info:
            raise ValueError(f"Unknown scale type: {scale_name}")
            
        scale_degrees = degrees[:scale_info['scale_degrees']]
        pattern = scale_info['interval_pattern']
        
        # Assign notes to degrees based on pattern
        for i, interval in enumerate(pattern):
            scale_degrees[i].assign_note(notes[interval])
            
        return ScaleFactory.create_scale(scale_name, scale_degrees[0].note, scale_degrees)