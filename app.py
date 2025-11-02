import json

from core import PianoCategory, PianoType, Piano
from services import PianoService
from config import AppConfig
from constants import REPO_TYPE_FILE


def load_config(file_path: str) -> AppConfig:
    try:
        with open(file_path, 'r') as file_reader:
            config_data = json.load(file_reader)
    
        return AppConfig(
            debug=config_data.get('debug', False),
            database_url=config_data.get('database_url', ''),
            repo_type=config_data.get('repo_type', REPO_TYPE_FILE)
        )
    
    
    except FileNotFoundError:
        print(f'Configuration file not found: {file_path}')
        return None
    
    except json.JSONDecodeError:
        print(f'Error decoding JSON from config file: {file_path}')
        return None
    
    except Exception as ex:
        print(f'An unexpected error occured: {ex}.')
        return None

        


def main():
    config = load_config()
    pass



piano = Piano(1, category='acoustic', piano_type='upright', name='Petrof', description='Petrof upright piano', basic_purpose='home and school use')

print(piano)


if __name__ == "__main__":
    main()