"""
THE NOTE CLASS
"""


class Note:
    """name: the name of the note, key: the key of the note"""
    def __init__(self, name: str, key: str):
        """
        Initialize a Note instance.

        :param name: The name of the note
        :param key: The key of the note
        """
        self.name = name
        self.key = key
