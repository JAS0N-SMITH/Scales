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


# MAKE MAJOR SCALE PATTERN
def major_scale(note_list, degree_list):
    """assigns correct notes to scale degrees"""
    major_scale_degrees = [degree_list[0], degree_list[1], degree_list[2], degree_list[3],
                           degree_list[4], degree_list[5], degree_list[6]]
    major_scale_pattern = [note_list[0], note_list[2], note_list[4], note_list[5],
                           note_list[7], note_list[9], note_list[11]]
    for k in range(0, len(major_scale_pattern)):
        major_scale_degrees[k].assign_note(major_scale_pattern[k])
    return Scale(f"{major_scale_degrees[0].note.name} Major Scale",
                 major_scale_degrees[0].note,
                 major_scale_degrees)


def minor_scale(note_list, degree_list):
    """assigns correct notes to scale degrees for minor scale"""
    minor_scale_degrees = [degree_list[0], degree_list[1], degree_list[2], degree_list[3],
                           degree_list[4], degree_list[5], degree_list[6]]
    minor_scale_pattern = [note_list[0], note_list[2], note_list[3], note_list[5],
                           note_list[7], note_list[8], note_list[10]]
    for k in range(0, len(minor_scale_pattern)):
        minor_scale_degrees[k].assign_note(minor_scale_pattern[k])
    return Scale(f"{minor_scale_degrees[0].note.name} Minor Scale",
                 minor_scale_degrees[0].note,
                 minor_scale_degrees)


major_scale = major_scale(organize_list(search_key), degrees)
print(major_scale.name)
for i in range(0, len(major_scale.degrees)):
    print(f"{major_scale.degrees[i].symbol}: {major_scale.degrees[i].note.name}")

minor_scale = minor_scale(organize_list(search_key), degrees)
print(minor_scale.name)
for i in range(0, len(minor_scale.degrees)):
    print(f"{minor_scale.degrees[i].symbol}: {minor_scale.degrees[i].note.name}")
