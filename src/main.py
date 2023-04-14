from pyvda import AppView

from DesktopManager import DesktopManager
from WebScapper import Scrapper

import helpers as h


def main():
    h.check_for_output_dir()

    desktopManager = DesktopManager()
    scrapper = Scrapper()

    new_desktop = desktopManager.create_desktop()

    scrapper.open_browser(
        move_callback=lambda: desktopManager.move_window(
            AppView(scrapper.browserWindowHWND), new_desktop
        )
    )

    scrapper.start()

    new_desktop.remove()


if __name__ == "__main__":
    main()
