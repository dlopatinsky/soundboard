from pathlib import Path

from config_module.config import Config
from gui_module.gui_application import ApplicationGui
from soundboard_module.soundboard import Soundboard

working_dir = Path(__file__).absolute().parent


class Main:
    def __init__(self, path: Path):
        self._config = Config(path)
        self._soundboard = Soundboard(self._config)

    def run(self):
        application_gui = ApplicationGui(self._soundboard, self._config)
        application_gui.run()


if __name__ == "__main__":
    config_dir = Path(f'{working_dir}/../config')
    main = Main(config_dir)
    main.run()
