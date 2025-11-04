import json
from core.pianos.pianos import Piano


class PianoRepo:
    def __init__(self, repo_type: str):
        self.repo_type = repo_type
        self._file_path = ''
        self.db_connection = ''
        self._configure(repo_type)
        
    
    def _configure(self, repo_type: str):
        if repo_type == 'file':
            self._file_path = 'data_store/files/pianos.json'
        elif repo_type == 'db':
            self._db_connection_string = 'database_connection_string'

    
    def get_all_pianos(self):
        pianos = []
        if self.repo_type == 'file':
            pianos = self._read_pianos_from_file()
            pianos = [dict_to_piano(piano) for piano in pianos]

        elif self.repo_type == 'db':
            # Implement database retrieval logic here
            pass
        return pianos
    
    
    def save_piano(self, piano: Piano) -> Piano:
        if self.repo_type == 'file':
            pianos = self._read_pianos_from_file()
            pianos.append(piano._to_dict())
            with open(self._file_path, 'w') as file_writer:
                json.dump(pianos, file_writer, indent=4)
            return piano
        elif self.repo_type == 'db':
            pass
    
    def _read_pianos_from_file (self):
        try:
            with open(self._file_path, 'r') as file_reader:
                piano_data =json.load(file_reader)
                if len(piano_data) == 0:
                    return []
                elif len(piano_data) == 1:
                    return piano_data
                return piano_data
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
        except Exception as ex:
            print (f'An unexpected exception occured while reading pianos file: {ex}')
            return []


def dict_to_piano(dictionary):
    return Piano(   dictionary['id'],
                    dictionary['category'],
                    dictionary['piano_type'],
                    dictionary['name'],
                    dictionary['description'],
                    dictionary['basic_purpose']
    )    
            