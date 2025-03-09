# progression.py
from models.chord import Chord

class ChordProgression:
    def __init__(self, scale):
        self.scale = scale

    def generate(self, progression_pattern):
        chord_progression = []
        for degree_index, chord_type in progression_pattern:
            degree = self.scale.degrees[degree_index]
            chord_progression.append(Chord(degree.note.name, chord_type))
        return chord_progression

    def get_progression_patterns(self):
        if 'Major' in self.scale.name:
            return [
                # Common chord progressions for major scale
                [(0, 'major'), (3, 'major'), (4, 'major'), (0, 'major')],  # I - IV - V - I
                [(0, 'major'), (4, 'major'), (3, 'major'), (0, 'major')],  # I - V - IV - I
                [(0, 'major'), (1, 'minor'), (4, 'major'), (0, 'major')],  # I - ii - V - I
            ]
        elif 'Minor' in self.scale.name:
            return [
                # Common chord progressions for minor scale
                [(0, 'minor'), (3, 'minor'), (4, 'minor'), (0, 'minor')],  # i - iv - v - i
                [(0, 'minor'), (4, 'minor'), (3, 'minor'), (0, 'minor')],  # i - v - iv - i
                [(0, 'minor'), (1, 'diminished'), (4, 'minor'), (0, 'minor')],  # i - ii° - v - i
            ]
        else:
            # Default to a simple I - IV - V - I progression if scale type is unknown
            return [
                [(0, 'major'), (3, 'major'), (4, 'major'), (0, 'major')],  # I - IV - V - I
            ]