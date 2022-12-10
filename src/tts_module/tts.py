import os.path
from pathlib import Path
import torch

from config_module.config import Config


class TTS:
    def __init__(self, config: Config):
        self._config = config
        self._device = torch.device(self._config.get_from_tts_config('TTS Settings', 'device_name'))

    def set_device(self, device_name: str):
        self._device = torch.device(device_name)

    def run(self, text: str, profile: str, path: Path):
        model, _ = torch.hub.load(repo_or_dir=self._config.get_from_tts_config(profile, 'repository'),
                                  model=self._config.get_from_tts_config(profile, 'model'),
                                  language=self._config.get_from_tts_config(profile, 'language'),
                                  speaker=self._config.get_from_tts_config(profile, 'model_id'))
        model.to(self._device)
        if os.path.exists(text):
            os.remove(text)
        model.save_wav(text=text,
                       speaker=self._config.get_from_tts_config(profile, 'speaker'),
                       sample_rate=int(self._config.get_from_tts_config(profile, 'sample_rate')),
                       audio_path=str(path))
