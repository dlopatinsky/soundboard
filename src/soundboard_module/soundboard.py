from pathlib import Path

from audio_module.audio_player import AudioPlayer
from config_module.config import Config
from tts_module.tts import TTS


class Soundboard:
    def __init__(self, config: Config):
        self._config = config
        self._audio_player = AudioPlayer()
        self._tts = TTS(self._config)

    def play_sound(self, file_path: Path):
        try:
            self._audio_player.play_sound(file_path)
        except (Exception):
            raise Exception('Error playing the file.')

    def stop_all_sounds(self):
        self._audio_player.stop_all_sounds()

    def run_tts(self, text: str, profile: str, path: Path):
        try:
            self._tts.run(text, profile, path)
        except (Exception):
            raise Exception('Error processing TTS')
