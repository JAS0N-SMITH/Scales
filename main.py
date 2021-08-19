"""
MAIN
"""
from Note import Note
from Degree import Degree
from Scale import Scale
from Scale_Options import scale_options_dict

search_key = input("Input key: ")

notes = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
degree_symbols = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']


def note_builder(note_list):
    """creates all of the note objects and returns a list of notes """
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
            for x in range(index + 1, length):  # enumerate?
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

# mps = scale_options_dict.get('Minor Pentatonic Scale')
# print(scale_options_dict.keys())
# print(mps.keys())
# print(mps.get('scale_degrees'))

scale_name = input("Choose a scale")


def build_scale(scale_pattern, scale_degrees, scale_name):
    """populates scale object with notes from note list and degree requirements
    TODO:[consider-using-enumerate] & consider combining with build_patterns()"""
    for k in range(0, len(scale_pattern)):
        scale_degrees[k].assign_note(scale_pattern[k])
    return Scale(f"{scale_degrees[0].note.name} {scale_name}",
                 scale_degrees[0].note,
                 scale_degrees)


def build_patterns(scale_name, note_list):
    """uses the scale name input and note list to arrange the notes and degrees in accordance
    with the pattern stored in the scale_options_dict dictionary
    TODO: Clean up"""
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
for i in range(0, len(scale.degrees)):  # learn how to use enumerate
    print(f"{scale.degrees[i].symbol}: {scale.degrees[i].note.name}")
