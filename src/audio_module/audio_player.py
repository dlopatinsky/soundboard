from openal import oalOpen, oalQuit
from openal import Source as OALSource, AL_STOPPED
from pathlib import Path
from typing import List


class AudioPlayer:
    def __init__(self):
        self._audio_threads: List[(Path, OALSource)] = list()

    def get_audio_list(self):
        self._clean_threads()
        result = []
        for thread in self._audio_threads.copy():
            result.append(thread[0])
        return result

    def play_sound(self, file_path: Path):
        thread = (file_path, oalOpen(str(file_path)))
        self._audio_threads.append(thread)
        thread[1].play()

    def stop_all_sounds(self):
        for thread in self._audio_threads:
            thread[1].stop()
        self._clean_threads()

    def _clean_threads(self):
        for thread in self._audio_threads.copy():
            if thread[1].get_state() == AL_STOPPED:
                thread[1].destroy()
                self._audio_threads.remove(thread)

    def __del__(self):
        oalQuit()
