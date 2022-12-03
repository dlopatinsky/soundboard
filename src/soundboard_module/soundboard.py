from pathlib import Path

from src.audio_module.audio_player import AudioPlayer
from src.config_module.config import Config
from src.tts_module.tts import TTS


class Soundboard:
    def __init__(self, config: Config):
        self._config = config
        self._audio_player = AudioPlayer()
        self._tts = TTS(self._config)

    def play_sound(self, file_path: Path):
        self._audio_player.play_sound(file_path)

    def stop_all_sounds(self):
        self._audio_player.stop_all_sounds()

    def run_tts(self, text: str, profile: str, path: Path):
        self._tts.run(text, profile, path)
