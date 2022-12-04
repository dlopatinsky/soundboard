from pathlib import Path

import openal
import pytest

from src.audio_module.audio_player import AudioPlayer


@pytest.mark.parametrize('path, expected_exception', [('resources/test.txt', openal.OalError),
                                  ('resources/test.nonexistent', openal.OalError)])
def test_audio_player_play_sound_exceptions(path, expected_exception):
    with pytest.raises(expected_exception):
        audio_player = AudioPlayer()
        audio_player.play_sound(Path(path))


@pytest.mark.parametrize('path', [('resources/test.wav')])
def test_audio_player_play_sound_normal(path):
    audio_player = AudioPlayer()
    audio_player.play_sound(Path(path))


@pytest.mark.parametrize('paths', [(),
                                   (('resources/test.wav', 'resources/test1.wav', 'resources/test2.wav')),
                                   (('resources/test.wav', 'resources/test.wav', 'resources/test.wav'))])
def test_audio_player_get_audio_list(paths):
    expected_list = []
    audio_player = AudioPlayer()
    for path in paths:
        audio_player.play_sound(Path(path))
        expected_list.append(Path(path))
    assert audio_player.get_audio_list() == expected_list
