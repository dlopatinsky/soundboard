from pathlib import Path

import openal
import pytest

from src.audio_module.audio_player import AudioPlayer


@pytest.mark.parametrize('path, expected_exception', [('tests/resources/test.txt', openal.OalError),
                                  ('resources/test.nonexistent', openal.OalError)])
def test_audio_player_play_sound_exceptions(path, expected_exception):
    with pytest.raises(expected_exception):
        audio_player = AudioPlayer()
        audio_player.play_sound(Path(path))


@pytest.mark.parametrize('path', [('tests/resources/test.wav')])
def test_audio_player_play_sound_normal(path):
    audio_player = AudioPlayer()
    audio_player.play_sound(Path(path))


@pytest.mark.parametrize('paths', [(),
                                   (('tests/resources/test.wav', 'tests/resources/test1.wav', 'tests/resources/test2.wav')),
                                   (('tests/resources/test.wav', 'tests/resources/test.wav', 'tests/resources/test.wav'))])
def test_audio_player_get_audio_list(paths):
    expected_list = []
    audio_player = AudioPlayer()
    for path in paths:
        audio_player.play_sound(Path(path))
        expected_list.append(Path(path))
    result = audio_player.get_audio_list()
    assert result == expected_list
