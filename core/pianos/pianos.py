from typing import Dict
from .piano_categories import PianoCategory
from .piano_types import PianoType


class Piano:
    def __init__(self, 
                 id: int,
                 category: PianoCategory, 
                 piano_type: PianoType,
                 name:str,
                 description: str,
                 basic_purpose: str):
        self.id = id
        self.category = category
        self.piano_type = piano_type
        self.name = name
        self.description = description
        self.basic_purpose = basic_purpose
        self.is_deleted:bool = False


    def __repr__(self):
        return f"'{self.category}' '{self.piano_type}' '{self.name}' piano for '{self.description}'."
    

    def _to_dict(self) -> Dict:
        return {
            "id": self.id,
            "category": self.category.to_dict(),
            "piano_type": self.piano_type.to_dict(),
            "name": self.name,
            "description": self.description,
            "basic_purpose": self.basic_purpose,
            "is_deleted": self.is_deleted   
        }   
    
    