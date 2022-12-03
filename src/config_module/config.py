from pathlib import Path
from configparser import ConfigParser


class Config:
    def __init__(self, path: Path):
        self._config = ConfigParser()

    def load(self, path: Path):
        self._config.read(path)

    def get_from_soundboard_config(self, section: str, option: str):
        try:
            return self._config[section][option]
        except:
            return self._get_default_soundboard_config()[section][option]

    def get_tts_profiles(self):
        profiles = list(dict(self._config).keys())
        profiles.remove("TTS Settings")
        return profiles

    def get_from_tts_config(self, section: str, option: str):
        try:
            return self._config[section][option]
        except:
            return self._get_default_tts_config()[section][option]

    @staticmethod
    def _get_default_soundboard_config():
        soundboard_config = ConfigParser()

        soundboard_config['Soundboard'] = {
            'sound_folder': '../../sounds'
        }
        return soundboard_config

    @staticmethod
    def generate_default_soundboard_config():
        soundboard_config = Config._get_default_soundboard_config()
        with open('../../config/soundboard.ini', 'w') as f:
            soundboard_config.write(f)

    @staticmethod
    def _get_default_tts_config():
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

    @staticmethod
    def generate_default_tts_config():
        tts_config = Config._get_default_tts_config()
        with open('../../config/tts.ini', 'w') as f:
            tts_config.write(f)
