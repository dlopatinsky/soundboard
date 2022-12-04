from pathlib import Path

from src.config_module.config import Config
from src.gui_module.gui_application import ApplicationGui
from src.soundboard_module.soundboard import Soundboard


class Main:
    def __init__(self, config_dir: Path):
        self._config = Config(config_dir)
        self._soundboard = Soundboard(self._config)

    def run(self):
        application_gui = ApplicationGui(self._soundboard, self._config)
        application_gui.run()

if __name__ == "__main__":
    config_dir = Path('../config')
    main = Main(config_dir)
    main.run()
