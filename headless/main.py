from pyvda import AppView

from DesktopManager import DesktopManager
from WebScapper import Scrapper


def main():
    desktopManager = DesktopManager()
    scrapper = Scrapper()

    new_desktop = desktopManager.create_desktop()

    scrapper.open_browser()

    browser_window = AppView(scrapper.browserWindowHWND)
    desktopManager.move_window(browser_window, new_desktop)

    scrapper.start()

    new_desktop.remove()


if __name__ == "__main__":
    main()
