# Chord.py
class Chord:
    def __init__(self, root_note, chord_type):
        self.root_note = root_note
        self.chord_type = chord_type

    def __repr__(self):
        return f"{self.root_note} {self.chord_type}"