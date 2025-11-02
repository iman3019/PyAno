


class PianoCategory:
    def __init__(self, category: str):
        self.category = category

    def __repr__(self):
        return f"Piano category is: '{self.category}'"


    def to_dict(self):
        return {
            "category": self.category
        }



    # ACOUSTIC = "acoustic"
    # ELECTRIC = "electric"
    # GRAND = "grand"
    # UPRIGHT = "upright"
    # DIGITAL = "digital"
    # HYBRID = "hybrid"