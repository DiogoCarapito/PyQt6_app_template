# pylint: disable=E0611  # no-name-in-module
# pylint: disable=W0212  # access-member-before-definition

import os
import sys
from PyQt6.QtGui import QKeySequence, QShortcut


def func():
    return None


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def quit_shortcut(window):
    # Add Cmd+W shortcut to close the window
    close_shortcut = QShortcut(QKeySequence("Ctrl+W"), window)
    close_shortcut.activated.connect(window.close)

    # On macOS, also add the Command+W shortcut
    if sys.platform == "darwin":  # macOS
        mac_close_shortcut = QShortcut(QKeySequence("Cmd+W"), window)
        mac_close_shortcut.activated.connect(window.close)
