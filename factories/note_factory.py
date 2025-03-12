"""Note Factory"""

from models.note import Note

class NoteFactory:
    """
    A factory class for creating Note objects and scales.
    Methods
    -------
    create_note(name: str) -> Note
        Create a single note object with the given name.
    create_chromatic_scale() -> list[Note]
        Create a list of Note objects representing all notes in the chromatic scale.
    """

    @staticmethod
    def create_note(name: str) -> Note:
        """Create a single note object"""
        return Note(name, name)

    @staticmethod
    def create_chromatic_scale() -> list[Note]:
        """Create all notes in the chromatic scale"""
        notes = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
        return [NoteFactory.create_note(note) for note in notes]