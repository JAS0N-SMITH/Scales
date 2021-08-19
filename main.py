"""
MAIN
"""
from Note import Note
from Degree import Degree
from Scale import Scale

search_key = input("Input key: ")

notes = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
degree_symbols = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']


def note_builder(note_list):
    """creates all of the note objects"""
    C = Note(note_list[0], note_list[0])
    Db = Note(note_list[1], note_list[1])
    D = Note(note_list[2], note_list[2])
    Eb = Note(note_list[3], note_list[3])
    E = Note(note_list[4], note_list[4])
    F = Note(note_list[5], note_list[5])
    Gb = Note(note_list[6], note_list[6])
    G = Note(note_list[7], note_list[7])
    Ab = Note(note_list[8], note_list[8])
    A = Note(note_list[9], note_list[9])
    Bb = Note(note_list[10], note_list[10])
    B = Note(note_list[11], note_list[11])
    return [C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B]


notes = note_builder(notes)


def organize_list(key):
    """Takes user input and reorganizes the notes list to start with the note provided by the
    user"""
    for note in notes:
        if key == note.name:
            length = len(notes)
            index = notes.index(note)
            new_list = [note]
            for x in range(index + 1, length):
                new_list.append(notes[x])
            for j in range(0, index):
                new_list.append(notes[j])
            return new_list


def degree_builder():
    """creates enough Degree objects to cover the total number of Notes"""
    I = Degree('First', degree_symbols[0])
    II = Degree('Second', degree_symbols[1])
    III = Degree('Third', degree_symbols[2])
    IV = Degree('Fourth', degree_symbols[3])
    V = Degree('Fifth', degree_symbols[4])
    VI = Degree('Sixth', degree_symbols[5])
    VII = Degree('Seventh', degree_symbols[6])
    VIII = Degree('Eighth', degree_symbols[7])
    IX = Degree('Ninth', degree_symbols[8])
    X = Degree('Tenth', degree_symbols[9])
    XI = Degree('Eleventh', degree_symbols[10])
    XII = Degree('Twelfth', degree_symbols[11])
    return [I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XII]


degrees = degree_builder()

scale_options_dict = {
    'Major Scale': {
        'scale_degrees': 7,
        'interval_pattern': [0, 2, 4, 5, 7, 9, 11],
    },
    'Natural Minor Scale': {
        'scale_degrees': 7,
        'interval_pattern': [0, 2, 3, 5, 7, 8, 10],
    },
    'Major Pentatonic Scale': {
        'scale_degrees': 5,
        'interval_pattern': [0, 2, 4, 7, 9],
    },
    'Minor Pentatonic Scale': {
        'scale_degrees': 5,
        'interval_pattern': [0, 3, 5, 7, 10],
    },
    'Blues Scale': {
        'scale_degrees': 6,
        'interval_pattern': [0, 3, 5, 6, 7, 10],
    },
    'Mixolydian Mode': {
        'scale_degrees': 7,
        'interval_pattern': [0, 2, 4, 5, 7, 9, 10],
    },
    'Lydian Mode': {
        'scale_degrees': 7,
        'interval_pattern': [0, 2, 4, 6, 7, 9, 11],
    },
    'Locrian Mode': {
        'scale_degrees': 7,
        'interval_pattern': [0, 1, 3, 5, 6, 8, 10],
    },
    'Dorian Mode': {
        'scale_degrees': 7,
        'interval_pattern': [0, 2, 3, 5, 7, 9, 10],
    },
    'Phrygian Mode': {
        'scale_degrees': 7,
        'interval_pattern': [0, 1, 3, 5, 7, 8, 10],
    },
    'Phrygian Dominant Scale': {
        'scale_degrees': 7,
        'interval_pattern': [0, 1, 4, 5, 7, 8, 10],
    }
}

# mps = scale_options_dict.get('Minor Pentatonic Scale')
# print(scale_options_dict.keys())
# print(mps.keys())
# print(mps.get('scale_degrees'))

scale_name = input("Choose a scale")


def build_scale(scale_pattern, scale_degrees, scale_name):
    """populates scale object with notes from note list and degree requirements"""
    for k in range(0, len(scale_pattern)):
        scale_degrees[k].assign_note(scale_pattern[k])
    return Scale(f"{scale_degrees[0].note.name} {scale_name}",
                 scale_degrees[0].note,
                 scale_degrees)


def build_patterns(scale_name, note_list):
    new_scale = scale_options_dict.get(scale_name)
    degrees_list = []
    for k in range(0, new_scale.get('scale_degrees')):
        degrees_list.append(degrees[k])
    interval_pattern = new_scale.get('interval_pattern')
    interval_pattern_list = []
    for interval in interval_pattern:
        interval_pattern_list.append(note_list[interval])
    return build_scale(interval_pattern_list, degrees_list, scale_name)


scale = build_patterns(scale_name, organize_list(search_key))
print(scale.name)
for i in range(0, len(scale.degrees)):
    print(f"{scale.degrees[i].symbol}: {scale.degrees[i].note.name}")
