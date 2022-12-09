from pathlib import Path

import pytest

from src.config_module.config import Config


@pytest.mark.parametrize('section, option, expected_value', [('TTS Settings', 'device_name', 'cpu'),
                                                             ('English non-default', 'language', 'en'),
                                                             ('English', 'sample_rate', '24000'),
                                                             ('Russian', 'language', 'ru')])
def test_config_get_from_tts_config_normal(section, option, expected_value):
    config = Config(Path('tests/test-config'))
    assert config.get_from_tts_config(section, option) == expected_value


@pytest.mark.parametrize('section, option, expected_value', [('Soundboard non-default', 'sounds', 'sounds'),
                                                             ('Soundboard', 'sound_folder', '../sounds')])
def test_config_get_from_soundboard_config_normal(section, option, expected_value):
    config = Config(Path('tests/test-config'))
    assert config.get_from_soundboard_config(section, option) == expected_value


@pytest.mark.parametrize('section, option, expected_value', [('Soundboard', 'sound_folder', '../sounds')])
def test_config_get_from_soundboard_config_auto_generated(section, option, expected_value):
    config = Config(Path('tests/config'))
    assert config.get_from_soundboard_config(section, option) == expected_value


@pytest.mark.parametrize('section, option, expected_value', [('TTS Settings', 'device_name', 'cpu'),
                                                             ('English', 'sample_rate', '24000')])
def test_config_get_from_tts_config_auto_generated(section, option, expected_value):
    config = Config(Path('tests/config'))
    assert config.get_from_tts_config(section, option) == expected_value


@pytest.mark.parametrize('section, option, expected_exception', [('Section', 'option', KeyError)])
def test_config_get_from_soundboard_config_exception(section, option, expected_exception):
    with pytest.raises(expected_exception):
        config = Config(Path('tests/config'))
        config.get_from_soundboard_config(section, option)
