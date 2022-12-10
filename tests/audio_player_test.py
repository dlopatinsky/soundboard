from pathlib import Path

import openal
import pytest

from src.audio_module.audio_player import AudioPlayer

working_dir = Path(__file__).absolute().parent

audio_player = AudioPlayer()


@pytest.mark.parametrize('sound_file, expected_exception', [('test.txt', openal.OalError),
                                                            ('test.nonexistent', openal.OalError)])
def test_audio_player_play_sound_exceptions(sound_file, expected_exception):
    audio_player.stop_all_sounds()
    with pytest.raises(expected_exception):
        audio_player.play_sound(Path(f'{working_dir}/resources/' + sound_file))


@pytest.mark.parametrize('sound_file', ['test.wav'])
def test_audio_player_play_sound_normal(sound_file):
    audio_player.stop_all_sounds()
    audio_player.play_sound(Path(f'{working_dir}/resources/' + sound_file))


@pytest.mark.parametrize('sound_files', [(),
                                         ('test.wav', 'test1.wav', 'test2.wav'),
                                         ('test.wav', 'test.wav', 'test.wav')])
def test_audio_player_get_audio_list(sound_files):
    audio_player.stop_all_sounds()
    expected_list = []
    for sound_file in sound_files:
        path = Path(f'{working_dir}/resources/' + sound_file)
        audio_player.play_sound(path)
        expected_list.append(path)
    result = audio_player.get_audio_list()
    assert result == expected_list
