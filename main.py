"""
MAIN
"""
from typing import Dict, List

from factories.note_factory import NoteFactory
from factories.degree_factory import DegreeFactory
from factories.scale_factory import ScaleFactory
from models.progression import ChordProgression
from models.scale import Scale

# initialize notes and degrees
notes = NoteFactory.create_chromatic_scale()
degrees = DegreeFactory.create_all_degrees()


def organize_list(key: str) -> List:
    """
    Reorganizes the notes list to start with the provided tonic note
    
    Args:
        key: The tonic note to start the scale with
        
    Returns:
        List of notes starting with the tonic
    """
    for note in notes:
        if key == note.name:
            length = len(notes)
            index = notes.index(note)
            return notes[index:length] + notes[0:index]
    raise ValueError(f"Invalid tonic note: {key}")    

def list_scales() -> List[str]:
    """
    Lists all available scales and returns their names
    
    Returns:
        List of scale names
    """
    from config.scale_options import scale_options_dict
    scales = list(scale_options_dict.keys())
    
    for i, scale in enumerate(scales, 1):
        print(f"\t{i}. {scale}")
    return scales

def main_menu() -> Dict[str, str]:
    """
    Displays the main menu and handles user input
    
    Returns:
        Dictionary containing selected tonic and scale name
    """
    print("Welcome to the Musical Scale Machine!")
    print("Please enter a tonic and choose from one of the following scales...")
    
    try:
        scales = list_scales()
        input_tonic = input("Tonic (eg. A, Eb, Gb, B): ").title()
        choice = int(input("Scale (eg. 1, 2, 3...): "))
        
        if not 1 <= choice <= len(scales):
            raise ValueError(f"Invalid scale selection: {choice}")
            
        return {
            'tonic': input_tonic,
            'scale_name': scales[choice - 1]
        }
    except ValueError as e:
        raise ValueError("Invalid input. Please try again.") from e

def display_chord_progressions(scale: Scale)-> None:
    """
    Displays available chord progressions for the given scale
    
    Args:
        scale: The scale to generate progressions from
    """
    chord_progression = ChordProgression(scale)
    progression_patterns = chord_progression.get_progression_patterns()
    print(f"Chord Progressions for {scale.name}:")
    for i, pattern in enumerate(progression_patterns, 1):
        progression = chord_progression.generate(pattern)
        print(f"Progression {i}: {' - '.join(str(chord) for chord in progression)}")

def display_scale(scale: Scale) -> None:
    """
    Displays the scale name and its degrees
    
    Args:
        scale: The scale to display
    """
    print(f"\n{scale.name}")
    for degree in scale.degrees:
        print(f"{degree.symbol}: {degree.note.name}")

def main() -> None:
    """ Main program loop """
    try:
        selection = main_menu()
        scale_name = selection['scale_name']
        tonic = selection['tonic']
        
        # Create scale using factories
        note_list = organize_list(tonic)
        scale = ScaleFactory.create_from_pattern(scale_name, note_list, degrees)
        
        # Display results
        display_scale(scale)
        display_chord_progressions(scale)
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
if __name__ == "__main__": 
    main()