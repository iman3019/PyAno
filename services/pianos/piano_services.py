from config import AppConfig
from infrastructure.pianos import PianoRepo
from core.pianos.pianos import Piano


class PianoService:
    def __init__(self, app_config: AppConfig):
        self.pianos = []
        self.app_config = app_config
        self.repo = PianoRepo(app_config.repo_type)

    
    def create_piano(self, piano: Piano):
        return self.repo.save_piano(piano)

    
    def get_piano(self, piano_id: int, is_deleted: bool = False):
        for piano in self.pianos:
            if piano.id == piano_id and piano.is_deleted == is_deleted:
                return piano
        return None
    
    def get_all_pianos(self, is_deleted: bool = False ):
        return [piano for piano in self.pianos if piano.is_deleted == is_deleted]

    def update_piano(self, piano_id: int, piano: Piano, is_deleted: bool = False):
        for piano in self.pianos:
            if piano.id == piano_id:
                piano.is_deleted = is_deleted
                piano = Piano()
                return self.create_piano (piano)

        return None


    def delete_piano(self, piano_id: int):
        piano = self.get_piano(piano_id)
        if piano:
            piano.is_deleted = True
            return piano
        return None