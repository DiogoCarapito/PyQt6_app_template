# pylint: disable=no-name-in-module

from PyQt6.QtWidgets import (
    QDockWidget,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QSpacerItem,
    QSizePolicy,
    QToolBar,
    QMenu,
    QToolButton,
)
from PyQt6.QtGui import QFont, QAction
from PyQt6.QtCore import Qt, QSize
from utils.icons import create_icon_from_svg, ICON_HOME, ICON_REFRESH, ICON_SETTINGS


def create_top_toolbar(window, change_page_func, home_page_class):
    # Create a toolbar
    toolbar = QToolBar("Main Toolbar")
    toolbar.setMovable(False)  # Make it non-movable
    toolbar.setIconSize(QSize(32, 32))  # Increase icon size
    toolbar.setObjectName("mainToolbar")  # Set object name for CSS styling

    # Home action with larger text and Pictogrammers icon
    home_icon = create_icon_from_svg(ICON_HOME)
    home_action = QAction(home_icon, "Home", window)
    home_action.triggered.connect(lambda: change_page_func(window, home_page_class))
    home_action.setStatusTip("Go to home page")
    home_button = QToolButton()
    home_button.setDefaultAction(home_action)
    home_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
    toolbar.addWidget(home_button)

    # Add a separator
    toolbar.addSeparator()

    # Refresh action with larger text and Pictogrammers icon
    refresh_icon = create_icon_from_svg(ICON_REFRESH)
    refresh_action = QAction(refresh_icon, "Refresh", window)
    refresh_action.setStatusTip("Refresh current page")
    refresh_button = QToolButton()
    refresh_button.setDefaultAction(refresh_action)
    refresh_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
    toolbar.addWidget(refresh_button)

    # Add spacer to push settings to the right
    spacer = QWidget()
    spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    toolbar.addWidget(spacer)

    # Settings action with dropdown menu and Pictogrammers icon
    settings_icon = create_icon_from_svg(ICON_SETTINGS)
    settings_action = QAction(settings_icon, "Settings", window)
    settings_action.setStatusTip("Open settings")

    # Create settings menu with larger text
    settings_menu = QMenu(window)
    settings_menu.setObjectName("settingsMenu")  # Set object name for CSS styling

    # Add menu items
    appearance_action = QAction("Appearance", window)
    preferences_action = QAction("Preferences", window)
    about_action = QAction("About", window)

    settings_menu.addAction(appearance_action)
    settings_menu.addAction(preferences_action)
    settings_menu.addSeparator()
    settings_menu.addAction(about_action)

    settings_action.setMenu(settings_menu)

    # Add settings button with text
    settings_button = QToolButton()
    settings_button.setDefaultAction(settings_action)
    settings_button.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
    settings_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

    # Set a minimum width for the settings button to accommodate the dropdown arrow
    settings_button.setMinimumWidth(120)

    # Add padding to the settings button
    settings_button.setStyleSheet("QToolButton { padding-right: 15px; }")

    toolbar.addWidget(settings_button)

    # Add the toolbar to the main window
    window.addToolBar(Qt.ToolBarArea.TopToolBarArea, toolbar)

    return toolbar


def create_navigation_sidebar(window, change_page_func, page1_class, page2_class):
    # Create a sidebar using QDockWidget without a title
    sidebar_dock = QDockWidget(window)
    sidebar_dock.setTitleBarWidget(QWidget())  # This removes the title bar
    sidebar_dock.setFeatures(
        QDockWidget.DockWidgetFeature.NoDockWidgetFeatures
    )  # Prevent undocking
    sidebar_dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea)
    sidebar_dock.setObjectName("navigationSidebar")  # Set object name for CSS styling

    # Create a widget to hold the navigation buttons
    nav_widget = QWidget()
    nav_widget.setObjectName("navWidget")  # Set object name for CSS styling

    nav_layout = QVBoxLayout(nav_widget)
    nav_layout.setContentsMargins(
        10, 20, 10, 10
    )  # Add some padding (left, top, right, bottom)

    # Create navigation buttons with larger font
    page1_btn = QPushButton("Page 1")
    page2_btn = QPushButton("Page 2")

    # Set larger font size for buttons
    large_font = QFont()
    large_font.setPointSize(16)  # Increase font size
    large_font.setBold(True)  # Make it bold for better visibility

    page1_btn.setFont(large_font)
    page2_btn.setFont(large_font)

    # Make buttons wider
    page1_btn.setMinimumWidth(150)
    page2_btn.setMinimumWidth(150)

    # Set object names for CSS styling
    page1_btn.setObjectName("navButton")
    page2_btn.setObjectName("navButton")

    # Connect button signals to change pages
    page1_btn.clicked.connect(lambda: change_page_func(window, page1_class))
    page2_btn.clicked.connect(lambda: change_page_func(window, page2_class))

    # Add buttons to layout with some spacing
    nav_layout.addWidget(page1_btn, 0, Qt.AlignmentFlag.AlignCenter)
    nav_layout.addSpacing(15)  # Add spacing between buttons
    nav_layout.addWidget(page2_btn, 0, Qt.AlignmentFlag.AlignCenter)

    # Add bottom spacer to push everything to the top
    nav_layout.addSpacerItem(
        QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
    )

    # Set the widget as the dock widget's content
    sidebar_dock.setWidget(nav_widget)

    # Add the dock widget to the main window
    window.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, sidebar_dock)

    # Set the dock widget width to 12% of the window width
    sidebar_dock.setFixedWidth(int(window.width() * 0.12))

    return sidebar_dock
