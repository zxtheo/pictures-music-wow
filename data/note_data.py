#note_data

class NoteData:
    def __init__(self, pitch, length, rest):
        self.pitch = pitch
        self.length = length
        self.rest = rest

    def to_list(self):
        return [self.pitch, self.length, self.rest]
    