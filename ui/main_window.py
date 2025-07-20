from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton


def create_main_window():
    window = QMainWindow()
    window.setWindowTitle("Simple PyQt6 Application")
    window.setGeometry(0, 0, 1920, 1080)

    central_widget = QWidget()
    window.setCentralWidget(central_widget)
    layout = QVBoxLayout()

    label = QLabel("Welcome to the Simple PyQt6 Application!")
    layout.addWidget(label)

    # add button
    button = QPushButton("Click Me")
    button.clicked.connect(lambda: label.setText("Button Clicked!"))
    layout.addWidget(button)

    central_widget.setLayout(layout)
    return window
