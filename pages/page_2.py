# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt


class Page2(QWidget):
    def __init__(self, title="Page 2"):
        super().__init__()

        # Create a layout
        layout = QVBoxLayout()

        # Create a title label
        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")

        # Add title to layout
        layout.addWidget(title_label)

        # Add some spacing
        layout.addSpacing(20)

        # Set the layout
        self.setLayout(layout)
