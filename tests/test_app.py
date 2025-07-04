# pylint: disable=no-name-in-module

import os
import sys

# import pytest

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QTimer


def test_window_creation():
    # Skip this test if running on GitHub Actions and we can't set up the environment properly
    if os.environ.get("GITHUB_ACTIONS") and sys.platform.startswith("linux"):
        # Set the QT_QPA_PLATFORM environment variable to 'offscreen'
        os.environ["QT_QPA_PLATFORM"] = "offscreen"
        # Also set XDG_RUNTIME_DIR which might be needed
        if "XDG_RUNTIME_DIR" not in os.environ:
            os.environ["XDG_RUNTIME_DIR"] = "/tmp/runtime-runner"

    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)

    window = QWidget()
    window.show()
    assert window.isVisible()

    # Create a timer to close the window after a short delay
    timer = QTimer()
    timer.timeout.connect(app.quit)
    timer.start(100)  # 100ms is enough for testing

    # Start the event loop and wait for the timer to trigger
    app.exec()

    # Clean up
    window.close()
    app.deleteLater()
