import os
from pathlib import Path

import pytest

from src.config_module.config import Config

working_dir = Path(__file__).absolute().parent


@pytest.mark.parametrize('section, option, expected_value', [('TTS Settings', 'device_name', 'cpu'),
                                                             ('English non-default', 'language', 'en'),
                                                             ('English', 'sample_rate', '24000'),
                                                             ('Russian', 'language', 'ru')])
def test_config_get_from_tts_config_normal(section, option, expected_value):
    config = Config(Path(f'{working_dir}/test-config'))
    assert config.get_from_tts_config(section, option) == expected_value


@pytest.mark.parametrize('section, option, expected_value', [('Soundboard non-default', 'sounds', 'sounds'),
                                                             ('Soundboard', 'sound_directory', f'{working_dir.parent.parent}/sounds')])
def test_config_get_from_soundboard_config_normal(section, option, expected_value):
    config = Config(Path(f'{working_dir}/test-config'))
    assert Path(config.get_from_soundboard_config(section, option)) == Path(expected_value)


def clean_default_config():
    tts_config_path = Path(f'{working_dir}/config/tts.ini')
    if os.path.exists(tts_config_path):
        os.remove(tts_config_path)
    soundboard_config_path = Path(f'{working_dir}/config/soundboard.ini')
    if os.path.exists(soundboard_config_path):
        os.remove(soundboard_config_path)


@pytest.mark.parametrize('section, option, expected_value', [('Soundboard', 'sound_directory', f'{working_dir.parent.parent}/sounds')])
def test_config_get_from_soundboard_config_auto_generated(section, option, expected_value):
    config = Config(Path(f'{working_dir}/config'))
    assert Path(config.get_from_soundboard_config(section, option)) == Path(expected_value)
    clean_default_config()


@pytest.mark.parametrize('section, option, expected_value', [('TTS Settings', 'device_name', 'cpu'),
                                                             ('English', 'sample_rate', '24000')])
def test_config_get_from_tts_config_auto_generated(section, option, expected_value):
    config = Config(Path(f'{working_dir}/config'))
    assert config.get_from_tts_config(section, option) == expected_value
    clean_default_config()


@pytest.mark.parametrize('section, option, expected_exception', [('Section', 'option', KeyError)])
def test_config_get_from_soundboard_config_exception(section, option, expected_exception):
    with pytest.raises(expected_exception):
        config = Config(Path(f'{working_dir}/config'))
        config.get_from_soundboard_config(section, option)
