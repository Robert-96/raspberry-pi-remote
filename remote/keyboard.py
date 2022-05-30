import os

import pyautogui


class Keyboard:

    def __init__(self, debug=False):
        self._debug = debug

    def debug(self):
        self._debug = True

    def hotkey(self, keys):
        if not self._debug:
            pyautogui.hotkey(*keys)
        else:
            pass


KEYBOARD = Keyboard(debug=False)
