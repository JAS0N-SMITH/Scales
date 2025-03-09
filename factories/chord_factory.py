from models.chord import Chord
from models.note import Note

class ChordFactory:
    @staticmethod
    def create_chord(root_note: Note, chord_type: str) -> Chord:
        """Create a chord object"""
        return Chord(root_note.name, chord_type)