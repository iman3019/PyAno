


class PianoType:
    def __init__(self, piano_type: str):
        self.piano_type = piano_type

    def __repr__(self):
        return f" Piano type is '{self.piano_type}'"
    
    def to_dict(self):
        return {
            "piano_type": self.piano_type
        }





    # ACOUSTIC = "acoustic"
    # ELECTRIC = "electric"
    # DIGITAL = "digital"
    # GRAND = "grand"
    # UPRIGHT = "upright"