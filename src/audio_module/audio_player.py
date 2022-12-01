from openal import oalOpen, oalQuit
from openal import Source as OALSource, AL_STOPPED
from pathlib import Path
from typing import List


class AudioPlayer:
    def __init__(self):
        self._audio_threads: List[OALSource] = list()

    def get_audio_count(self) -> int:
        self._clean_threads()
        return len(self._audio_threads)

    def play_sound(self, file_path: Path):
        openal_thread = oalOpen(str(file_path))
        self._audio_threads.append(openal_thread)
        openal_thread.play()

    def stop_all_sounds(self):
        for openal_thread in self._audio_threads:
            openal_thread.stop()
        self._clean_threads()

    def _clean_threads(self):
        for thread in self._audio_threads.copy():
            if thread.get_state() == AL_STOPPED:
                thread.destroy()
                self._audio_threads.remove(thread)

    def exit(self):
        oalQuit()
