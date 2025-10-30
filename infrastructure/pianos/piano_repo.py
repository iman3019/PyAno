import json
from core.pianos.pianos import Piano


class PianoRepo:
    def __init__(self, repo_type: str):
        self.repo_type = repo_type
        self.file_path = ''
        self.db_connection = ''
        
    
    def _configure(self, repo_type: str):
        if repo_type == 'file':
            self._file_path = 'data_store/files/pianos.json'
        elif repo_type == 'db':
            self._db_connection_string = 'database_connection_string'

    def save_piano(self, piano: Piano) -> Piano:
        if self.repo_type == 'file':
            pianos = _read_pianos_from_file()

        
        with open(file, 'r') as file_reader
            json.load(  )

    
    def _read_pianos_from_file ():
        with open(file_path, 'r') as file_reader:
            pianos = 
            json.load(file_reader)