from pyvda import AppView, VirtualDesktop, get_apps_by_z_order, get_virtual_desktops

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


if __name__ == "__main__":
    main()
