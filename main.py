"""
MAIN
"""
from Note import Note
from Degree import Degree
from Scale import Scale

notes = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
degree_symbols = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']

C = Note(notes[0], notes[0])
Db = Note(notes[1], notes[1])
D = Note(notes[2], notes[2])
Eb = Note(notes[3], notes[3])
E = Note(notes[4], notes[4])
F = Note(notes[5], notes[5])
Gb = Note(notes[6], notes[6])
G = Note(notes[7], notes[7])
Ab = Note(notes[8], notes[8])
A = Note(notes[9], notes[9])
Bb = Note(notes[10], notes[10])
B = Note(notes[11], notes[11])

notes = [C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B]

search_key = input("Input key: ")


def organize_list(key):
    """Takes user input and reorganizes the notes list to start with the note provided by the
    user"""
    for note in notes:
        if key == note.name:
            length = len(notes)
            index = notes.index(note)
            new_list = [note]
            for i in range(index + 1, length):
                new_list.append(notes[i])
            for j in range(0, index):
                new_list.append(notes[j])
            return new_list


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


# degrees = [I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XII]

# MAKE MAJOR SCALE PATTERN
def major_scale(notes):
    """assigns correct notes to scale degrees"""
    major_scale_degrees = [I, II, III, IV, V, VI, VII]
    major_scale_pattern = [notes[0], notes[2], notes[4], notes[5],
                           notes[7], notes[9], notes[11]]
    for k in range(0, len(major_scale_pattern)):
        major_scale_degrees[k].assign_note(major_scale_pattern[k])
    major_scale = Scale(f"{I.note.name} Major Scale", I.note, major_scale_degrees)
    return major_scale


def minor_scale(notes):
    """assigns correct notes to scale degrees for minor scale"""
    minor_scale_degrees = [I, II, III, IV, V, VI, VII]
    minor_scale_pattern = [notes[0], notes[2], notes[3], notes[5],
                           notes[7], notes[8], notes[10]]
    for k in range(0, len(minor_scale_pattern)):
        minor_scale_degrees[k].assign_note(minor_scale_pattern[k])
    minor_scale = Scale(f"{I.note.name} Minor Scale", I.note, minor_scale_degrees)
    return minor_scale


major_scale = major_scale(organize_list(search_key))
print(major_scale.name)
for i in range(0, len(major_scale.degrees)):
    print(f"{major_scale.degrees[i].symbol}: {major_scale.degrees[i].note.name}")

minor_scale = minor_scale(organize_list(search_key))
print(minor_scale.name)
for i in range(0, len(minor_scale.degrees)):
    print(f"{minor_scale.degrees[i].symbol}: {minor_scale.degrees[i].note.name}")