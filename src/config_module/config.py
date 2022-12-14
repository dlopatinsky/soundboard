import os.path
from pathlib import Path
from configparser import ConfigParser


class Config:
    def __init__(self, path: Path):
        self._tts_config = ConfigParser()
        self._soundboard_config = ConfigParser()
        self.path = path
        self.load(path)

    def load(self, path: Path):
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
        tts_config_path = Path(f'{str(path)}/tts.ini')
        if not os.path.exists(tts_config_path):
            self.generate_default_tts_config(tts_config_path)
        self._tts_config.read(tts_config_path)
        soundboard_config_path = Path(f'{str(path)}/soundboard.ini')
        if not os.path.exists(soundboard_config_path):
            self.generate_default_soundboard_config(soundboard_config_path)
        self._soundboard_config.read(soundboard_config_path)

    def get_from_soundboard_config(self, section: str, option: str):
        try:
            return self._soundboard_config[section][option]
        except (Exception):
            return self._get_default_soundboard_config()[section][option]

    def get_tts_profiles(self):
        profiles = list(dict(self._tts_config).keys())
        excluded_sections = ['TTS Settings', 'DEFAULT']
        for section in excluded_sections:
            if section in profiles:
                profiles.remove(section)
        return profiles

    def get_from_tts_config(self, section: str, option: str):
        try:
            return self._tts_config[section][option]
        except (Exception):
            return self._get_default_tts_config()[section][option]

    def _get_default_soundboard_config(self):
        soundboard_config = ConfigParser()

        soundboard_config['Soundboard'] = {
            'sound_directory': f'{self.path.parent.parent.parent}/sounds'
        }
        return soundboard_config

    def generate_default_soundboard_config(self, path: Path):
        soundboard_config = Config._get_default_soundboard_config(self)
        with open(path, 'w') as f:
            soundboard_config.write(f)

    def _get_default_tts_config(self):
        tts_config = ConfigParser()

        tts_config['TTS Settings'] = {
            'device_name': 'cpu'
        }

        tts_config['Russian'] = {
            'repository': 'snakers4/silero-models',
            'model': 'silero_tts',
            'language': 'ru',
            'model_id': 'v3_1_ru',
            'speaker': 'aidar',
            'sample_rate': 24000
        }

        tts_config['English'] = {
            'repository': 'snakers4/silero-models',
            'model': 'silero_tts',
            'language': 'en',
            'model_id': 'v3_en',
            'speaker': 'en_1',
            'sample_rate': 24000
        }
        return tts_config

    def generate_default_tts_config(self, path: Path):
        tts_config = Config._get_default_tts_config(self)
        with open(path, 'w') as f:
            tts_config.write(f)
