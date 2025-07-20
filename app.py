# pylint: disable=E0611  # no-name-in-module

import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from ui.main_window import create_main_window as mainWindow

from utils.utils import resource_path, quit_shortcut


def create_app():
    app = QApplication(sys.argv)

    icon_path = "icon.png"
    app.setWindowIcon(QIcon(resource_path(icon_path)))

    window = mainWindow()
    quit_shortcut(window)

    return app, window


def main():
    app, window = create_app()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
