"""
### Pyvda Desktop Manager Wrapper and Helper Functions
"""

from dataclasses import dataclass
from pyvda import AppView, VirtualDesktop, get_apps_by_z_order, get_virtual_desktops


@dataclass
class DesktopManager:
    """
    DesktopManager is a wrapper for pyvda that provides helper functions for managing virtual desktops.
    """

    def __post_init__(self):
        pass

    def get_number_of_desktops(self):
        return len(get_virtual_desktops())

    def get_current_desktop(self):
        return VirtualDesktop.current()

    def get_current_window(self):
        return AppView.current()

    def get_target_desktop(self):
        return VirtualDesktop(1).create()

    def move_window(self, target_window: AppView, target_desktop: VirtualDesktop):
        """Moves a window to a target desktop.

        Args:
            target_window (AppView): Target window to move.
            target_desktop (VirtualDesktop): Target desktop to move the window to.
        """

        target_window.move(target_desktop)
        print(f"Moved window {target_window.hwnd} to {target_desktop.number}")

    def go_to_desktop(self, target_desktop: VirtualDesktop):
        """Go to a target desktop.

        Args:
            target_desktop (VirtualDesktop): Target desktop to go to.
        """

        target_desktop.go()

    def remove_desktop(self, target_desktop: VirtualDesktop):
        """Remove a target desktop.

        Args:
            target_desktop (VirtualDesktop): Target desktop to remove.
        """

        target_desktop.remove()
