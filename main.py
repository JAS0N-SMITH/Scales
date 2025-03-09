"""
MAIN
"""
from models.note import Note
from models.degree import Degree
from models.scale import Scale
# from models.chord import Chord
from config.scale_options import scale_options_dict
from models.progression import ChordProgression

notes = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
degree_symbols = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']


def note_builder(note_list):
    """creates all of the note objects and returns a list of notes """
    c_note = Note(note_list[0], note_list[0])
    d_flat_note = Note(note_list[1], note_list[1])
    d_note = Note(note_list[2], note_list[2])
    e_flat_note = Note(note_list[3], note_list[3])
    e_note = Note(note_list[4], note_list[4])
    f_note = Note(note_list[5], note_list[5])
    g_flat_note = Note(note_list[6], note_list[6])
    g_note = Note(note_list[7], note_list[7])
    a_flat_note = Note(note_list[8], note_list[8])
    a_note = Note(note_list[9], note_list[9])
    b_flat_note = Note(note_list[10], note_list[10])
    b_note = Note(note_list[11], note_list[11])
    return [c_note, d_flat_note, d_note, e_flat_note, e_note, f_note,
            g_flat_note, g_note, a_flat_note, a_note, b_flat_note, b_note]


notes = note_builder(notes)


def organize_list(key):
    """Takes user input and reorganizes the notes list to start with the note provided by the user"""
    for note in notes:
        if key == note.name:
            length = len(notes)
            index = notes.index(note)
            new_list = [note]
            for j in range(index + 1, length):
                new_list.append(notes[j])
            for k in range(0, index):
                new_list.append(notes[k])
    return new_list


def degree_builder():
    """creates enough Degree objects to cover the total number of Notes"""
    first_degree = Degree('First', degree_symbols[0])
    second_degree = Degree('Second', degree_symbols[1])
    third_degree = Degree('Third', degree_symbols[2])
    fourth_degree = Degree('Fourth', degree_symbols[3])
    fifth_degree = Degree('Fifth', degree_symbols[4])
    sixth_degree = Degree('Sixth', degree_symbols[5])
    seventh_degree = Degree('Seventh', degree_symbols[6])
    eighth_degree = Degree('Eighth', degree_symbols[7])
    ninth_degree = Degree('Ninth', degree_symbols[8])
    tenth_degree = Degree('Tenth', degree_symbols[9])
    eleventh_degree = Degree('Eleventh', degree_symbols[10])
    twelfth_degree = Degree('Twelfth', degree_symbols[11])
    return [first_degree, second_degree, third_degree, fourth_degree,
            fifth_degree, sixth_degree, seventh_degree, eighth_degree,
            ninth_degree, tenth_degree, eleventh_degree, twelfth_degree]


degrees = degree_builder()


def build_scale(scale_pattern, scale_degrees, s_name):
    """populates scale object with notes from note list and degree requirements"""
    for k, note in enumerate(scale_pattern):
        scale_degrees[k].assign_note(note)
    return Scale(f"{scale_degrees[0].note.name} {s_name}",
                 scale_degrees[0].note,
                 scale_degrees)


def build_patterns(s_name, note_list):
    """uses the scale name input and note list to arrange the notes and degrees in accordance with the pattern stored in the scale_options_dict dictionary"""
    new_scale = scale_options_dict.get(s_name)
    degrees_list = []
    for k in range(0, new_scale.get('scale_degrees')):
        degrees_list.append(degrees[k])
    interval_pattern = new_scale.get('interval_pattern')
    interval_pattern_list = []
    for interval in interval_pattern:
        interval_pattern_list.append(note_list[interval])
    return build_scale(interval_pattern_list, degrees_list, s_name)


def list_scales():
    """lists all available scales in dict"""
    string_split = scale_options_dict.keys().__str__()
    txt = string_split.split("[")
    txt = txt[1].split("]")
    txt = txt[0].split(", ")
    for txts in txt:
        s_name = txts.strip("'")
        print(f"\t{txt.index(txts) + 1}. {s_name}")
    return txt


def main_menu():
    """do the menu thing again"""
    print("Welcome to the Musical Scale Machine!\n\tPlease enter a tonic and choose from one of the following scales...")
    scales = list_scales()
    input_tonic = input("Tonic (eg. A, Eb, Gb, B): ").title()
    choice = int(input("Scale (eg. 1, 2, 3...): "))
    menu_selection = {'tonic': input_tonic,
                      'scale_name': scales[choice - 1]}
    return menu_selection


def display_chord_progressions(scale):
    """Displays multiple chord progressions for the given scale"""
    chord_progression = ChordProgression(scale)
    progression_patterns = chord_progression.get_progression_patterns()
    print(f"Chord Progressions for {scale.name}:")
    for i, pattern in enumerate(progression_patterns):
        progression = chord_progression.generate(pattern)
        print(f"Progression {i + 1}: {' - '.join(str(chord) for chord in progression)}")


def main():
    selection = main_menu()
    scale_name = selection.get("scale_name").strip("'")
    tonic = selection.get("tonic").strip("'")
    scale = build_patterns(scale_name, organize_list(tonic))
    print(scale.name)
    for i, degree in enumerate(scale.degrees):
        print(f"{degree.symbol}: {degree.note.name}")
    display_chord_progressions(scale)


if __name__ == "__main__":
    main()
