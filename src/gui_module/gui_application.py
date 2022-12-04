import os
from pathlib import Path

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

from src.config_module.config import Config
from src.soundboard_module.soundboard import Soundboard


class ApplicationGui(App):
    def __init__(self, soundboard: Soundboard, config: Config, **kwargs):
        super().__init__(**kwargs)
        self._soundboard = soundboard
        self._config = config
        self._sound_folder = Path(self._config.get_from_soundboard_config('Soundboard', 'sound_folder'))

        # Sound list
        self._audio_file_list = GridLayout(padding=0, cols=1, size_hint_y=None)
        self._audio_file_list.bind(minimum_height=self._audio_file_list.setter('height'))
        self.update_sound_list()

        # Menu
        self._tts_text = TextInput(multiline=False)
        self._profile_spinner = Spinner(values=self._config.get_tts_profiles())
        self._error_notification = Label(color='#880000')

    def build(self):
        root = GridLayout(padding=2, rows=1)

        sound_list = GridLayout(padding=5, cols=1)
        audio_list_scroll = ScrollView()
        audio_list_scroll.add_widget(self._audio_file_list)
        sound_list.add_widget(audio_list_scroll)

        menu = GridLayout(padding=0, cols=1)
        menu.add_widget(Label(text='Menu'))
        menu.add_widget(self._tts_text)
        run_tts_button = Button(text='Run TTS')
        run_tts_button.bind(on_press=self._run_tts)
        menu.add_widget(run_tts_button)
        menu.add_widget(self._profile_spinner)
        update_sounds_button = Button(text='Update sounds')
        update_sounds_button.bind(on_press=self.update_sound_list)
        menu.add_widget(update_sounds_button)
        stop_all_sounds_button = Button(text='Stop all sounds')
        stop_all_sounds_button.bind(on_press=self._stop_all_sounds)
        menu.add_widget(stop_all_sounds_button)
        menu.add_widget(self._error_notification)

        root.add_widget(sound_list)
        root.add_widget(menu)
        return root

    def update_sound_list(self, button: Button = 0):
        files = os.listdir(self._sound_folder)
        self._audio_file_list.clear_widgets()
        for file in files:
            button = Button(text=file, size_hint_y=None)
            button.bind(on_press=self._play_sound)
            self._audio_file_list.add_widget(button)

    def _run_tts(self, button: Button):
        text = self._tts_text.text
        path = Path(self._config.get_from_soundboard_config("Soundboard", "sound_folder") + '/' + text + '.wav')
        try:
            self._soundboard.run_tts(text, self._profile_spinner.text, path)
            self.update_sound_list()
        except (Exception):
            message = '''
            Error processing TTS!
            Please, make sure that a valid TTS profile is selected
            and the message language matches the profile.
            '''
            self._notify_error(message)

    def _play_sound(self, button: Button):
        path = Path(self._config.get_from_soundboard_config("Soundboard", "sound_folder") + '/' + button.text)
        try:
            self._soundboard.play_sound(path)
        except (Exception):
            message = '''
            Error playing the file!
            Please, make sure it\'s a .wav audio file.
            '''
            self._notify_error(message)

    def _notify_error(self, message: str):
        self._error_notification.text = message

    def _stop_all_sounds(self, button: Button = 0):
        self._soundboard.stop_all_sounds()
