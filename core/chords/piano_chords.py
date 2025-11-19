from sqlalchemy import Column, Integer, String

from infrastructure.database.database import Base
from config import NAME_LENGTH, DESCRIPTION_LENGTH, URL_LENGTH


class PianoChords(Base):
    __tablename__ = 'piano_chords'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(NAME_LENGTH), nullable=False)

    description = Column(String(DESCRIPTION_LENGTH), nullable=True)
    image_url = Column(String(URL_LENGTH), nullable=True)

    def __repr__(self):
        if self.id:
            return f'Piano chord: ({self.id}) {self.name}'
        else:
            return f'Piano chord: {self.name}'