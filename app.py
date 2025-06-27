# pylint: disable=no-name-in-module

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon, QKeySequence, QShortcut
import sys

# Import your page classes
from pages.page_1 import Page1
from pages.page_2 import Page2
from ui.ui import create_top_toolbar, create_navigation_sidebar


# Function to configure the application
def app_config():
    # Set the application name, organization name, and display name
    app = QApplication(sys.argv)
    app.setApplicationName("PyQt6 App Template")
    app.setOrganizationName("N/A")
    app.setApplicationDisplayName("PyQt6 App Template")

    # Set the application icon
    app.setWindowIcon(QIcon("assets/logo.png"))

    # Load the stylesheet
    with open("style.css", "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())

    return app


# Function to change the page - defined outside main() so it's available when needed
def change_page(window, page_class):
    # Create a new instance of the page
    page = page_class()

    # Set it as the central widget
    window.setCentralWidget(page)

    # Return the page instance for reference
    return page


def main():
    # Configure the application and start the event loop
    app = app_config()

    # Create a main window
    window = QMainWindow()
    window.resize(1920, 1080)
    window.setWindowTitle("PyQt6 App Template")

    # Add Cmd+W shortcut to close the window
    close_shortcut = QShortcut(QKeySequence("Ctrl+W"), window)
    close_shortcut.activated.connect(window.close)

    # On macOS, also add the Command+W shortcut
    if sys.platform == "darwin":  # macOS
        mac_close_shortcut = QShortcut(QKeySequence("Cmd+W"), window)
        mac_close_shortcut.activated.connect(window.close)

    # Create the top toolbar
    create_top_toolbar(window, change_page, Page1)

    # Create the navigation sidebar
    create_navigation_sidebar(window, change_page, Page1, Page2)

    # Set the initial page
    change_page(window, Page1)

    # Show the main window and start the event loop
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
