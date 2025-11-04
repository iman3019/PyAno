import json

from core import PianoCategory, PianoType, Piano
from services import PianoService
from config import AppConfig
from constants import REPO_TYPE_FILE, CONFIG_FILE_TYPE


def load_config(file_path: str) -> AppConfig:
    try:
        with open(file_path, 'r') as file_reader:
            config_data = dict(json.load(file_reader))
    
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
    app_config = load_config(CONFIG_FILE_TYPE)
    if app_config is None:
        print(f'Could not load config from file. Exiting.')
        return

    piano_service = PianoService(app_config)
    piano_acoustic = PianoCategory(category="acoustic")
    upright_piano = PianoType(piano_type="upright")
    petrof = Piano(id= 1,
                   category=piano_acoustic,
                   piano_type=upright_piano,
                   name="Petrof",
                   description="upright wooden acoustic piano",
                   basic_purpose="education and small hall playing")
    petrof = piano_service.create_piano(petrof)


    yamaha = Piano(id=2,
                   category=piano_acoustic,
                   piano_type=upright_piano,
                   name="Yamaha",
                   description="upright mdf acoustic piano",
                   basic_purpose=" home use")
    yamaha = piano_service.create_piano(yamaha)

    piano = Piano(1, category='acoustic', piano_type='upright', name='Petrof', description='Petrof upright piano', basic_purpose='home and school use')

    print(piano)

    all_pianos = piano_service.get_all_pianos()
    print(all_pianos)

if __name__ == "__main__":
    main()