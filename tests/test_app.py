# pylint: disable=no-name-in-module

import os

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QTimer


def test_window_creation():
    # Set the QT_QPA_PLATFORM environment variable to 'offscreen' if running in CI
    if os.environ.get("CI"):
        os.environ["QT_QPA_PLATFORM"] = "offscreen"

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
